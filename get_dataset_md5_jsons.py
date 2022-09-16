import argparse
import json 


def open_json(file_n):
    '''load the json file'''

    with open(file_n) as f:
        hg = json.load(f) #just one key = datasets 
        return hg
        #print hg['datasets'][0].keys()

        
def get_dsname(md5sum, hg):
    '''Receives a list of md5sum and a json file
    (i.e hg38-ihec-final.json). Returnn a 
    list of dataset names associated with each md5sum (if exist)'''

    list_hg38_dstname = [] #store the dataset name related with the md5sum from hg38 (to check in hg19 final json)
    
    for i in md5sum:

        md5 = i.strip()
        for ele in hg['datasets']:
            try:
                if ele['md5sum'] == md5:
                    list_hg38_dstname.append(ele['dataset_name'])
                
            except KeyError as e:
                continue

    return list_hg38_dstname


#lists to store the md5sum information from hg19 final json related with the dataset names from hg38 (overlap) and to store the dataset names with no match


def get_md5(list_dsname, hg2):
    '''Receives a list of dataset names
    and a json file (i.e hg19-ihec-final.json - third argument)
    Returns a list of md5sum associated with 
    each dataset name (if exist). If you want 
    to check the list of no match you can uncomment
    the  #print(list_no_match) on the main function'''

    list_hg19_md5 = []
    list_no_match = []
    
    for i in list_dsname:
        dset = i.strip()

        for ele in hg2['datasets']:
            try:
                if ele['dataset_name'] == dset:
                    list_hg19_md5.append(ele['md5sum'])

            except:
                list_no_match.append(ele['dataset_name'])
 

    return list_hg19_md5, list_no_match


def write_file(list_md5):
    '''write a txt file with 
    the md5sum for all matched
    files from hg38 in hg19'''
    
    with open('output1_md5.txt', 'w') as f:
        f.write('\n'.join(list_md5))
    

def main():
    hg = open_json(args.path)
    md5sum = open(args.list, 'r')
    list_hg38_dstname = get_dsname(md5sum, hg)
    hg2 = open_json(args.dest)
    list_hg19_md5, list_no_match = get_md5(list_hg38_dstname, hg2)
    write_file(list_hg19_md5)
    #print(len(list_hg19_md5))
    #print(list_no_match)
    

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(
        description = 'A script to find in a first moment the dataset name related to a list of md5sum obtained from a specific assembly/release/IHEC/final json files (project related with EpiLap).' 
        'The list of dataset names will be used to recover the md5sum information in the json files from another assembly/release (using the final json file)'
        'This script returns a txt file with the md5sum information related to the second assembly release that are inserted in the first assembly (i.e the md5sum of hg19 that matches hg38)'
        )
    
    parser.add_argument('-p', '--path', action="store",
                        help='root path to the final json (for instance hg38-2019-11_final.json) to get the dataset name from a list of md5sum '
        )
    
    parser.add_argument('-l', '--list', action="store",
                        help='root path to a list of md5sum obtained from one IHEC/final assembly-release json. For instance: list of md5sum from hg38.'
        )
    
    parser.add_argument('-d', '--dest', action="store",
                        help='root path to the final json (for instance hg19) to check if the dataset names from hg38 exist'
        )
    
    args = parser.parse_args()
    main()



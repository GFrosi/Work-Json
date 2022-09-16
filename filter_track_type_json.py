import json
import sys
import argparse



def open_json(file_n):
    '''load a json file'''

    with open(file_n) as f:
        hg = json.load(f) #just one key = datasets 
        return hg
      

def get_track_type(json_file, track):
    '''Receives a json file and the track_type.
    Returns two lists'''
    
    list_dset = []
    list_md5 = []
    
    for dset in json_file['datasets']:

        if 'pval' in track:
        
            try:
                if 'pval' in dset['track_type']:

                    list_dset.append(dset)
                    list_md5.append(dset['md5sum'])
                
                if 'input' in dset['assay']:

                    list_dset.append(dset)
                    list_md5.append(dset['md5sum'])
                
            except:
                continue 

        else:
            
            try:
                if track in dset['track_type'] and 'input' not in dset['assay']: #to avoid ctl_raw when track = raw

                    list_dset.append(dset)
                    list_md5.append(dset['md5sum'])
                
            except:
                continue 
    
  
    return list_dset, list_md5


def write_json(path, list_dset):
    '''Write content to json path'''
    with open(path, 'w') as f:
        json.dump({"datasets":list_dset}, f)


def write_txt(path, list_md5):
    '''write content to txt path'''
    
    with open(path, 'w') as fn:
        for item in list_md5:
            fn.write("%s\n" % item)



def main():

    j_work = open_json(args.path)
    list_dset, list_md5 = get_pval_input(j_work)
    write_json(args.dset, list_dset)
    write_txt(args.md5, list_md5)



if __name__ == '__main__':


    parser = argparse.ArgumentParser(
        description = 'A script to filter pval and input samples from a json file)'
        )


    parser.add_argument('-p', '--path', action="store",
                        help='root path to the json file'
        )

    parser.add_argument('-t', '--track', action="store",
                        help='name of the track_type (pval, fc or raw). When pval, the filtered json will contains the ctl_raw datasets.'
        )

    parser.add_argument('-d', '--dset', action="store",
                        help='root path to write the new json file'
        )

    parser.add_argument('-m', '--md5', action="store",
                        help='root path to write the md5 sum files in a txt file'
        )

    args = parser.parse_args()
    main()

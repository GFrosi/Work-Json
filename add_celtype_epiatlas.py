import json
import sys
import argparse
from tqdm import tqdm



def create_dict(ihec, epi):
    '''Receives two files with the md5sum 
    from Ihec and EpiAtlas samples. Returns 
    a dictionary where the keys are the md5sums
    from EpiAtlas and the values are the md5sum
    from IHEC'''
    
    dict_ihec_epi = {}
    
    fh1 = open(ihec, 'r')
    fh2 = open(epi, 'r')
   
    for ln1, ln2 in zip(fh1, fh2):
        ln1 = ln1.strip()
        ln2 = ln2.strip()
       
        dict_ihec_epi[ln2] = ln1
    
    return dict_ihec_epi


def cell_type_dset(ihec_j, epi_j, dict_ihec_epi):
    '''Receives two jsons (from ihec and epiatlas)
    and the dictionary with the md5sum information.
    Returns a list with all matches datasets including
    the cell_type information'''
    
    list_dset = []
    f = open(ihec_j)
    fn = open(epi_j)
    ihec_js = json.load(f)
    epi_js = json.load(fn)

    ihec_epi_keys = dict_ihec_epi.keys()
    
    for dset in tqdm(epi_js['datasets']):
    
        for i,sample in enumerate(ihec_js['datasets']):
    
            if dset['md5sum'] in ihec_epi_keys and dict_ihec_epi[dset['md5sum']] == sample['md5sum']:
                #print('dest:',dset['md5sum'], 'dict_value:', dict_ihec_epi[dset['md5sum']], 'sample:',  sample['md5sum'])

                dset['cell_type'] = sample['cell_type']
                list_dset.append(dset)
                break
            
            if i == (len(ihec_js['datasets']) -1):
                list_dset.append(dset)

    return list_dset        


def write_json(path, list_dset):
    '''Write content to json path'''
    
    with open(path, 'w') as f:
        json.dump({"datasets":list_dset}, f)


def main():

    dict_ihec_epi = create_dict(args.ihec,args.epi)
    #print(len(dict_ihec_epi))
    list_dset = cell_type_dset(args.fjson,args.fJSON, dict_ihec_epi)
    write_json(args.output, list_dset)


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(
        description="A script to add the cell_type key from the ihec_final json to epiatlas json.")

    parser.add_argument('-i', '--ihec', action="store",
                        help='The root path to a file with the md5sum from ihec samples that matched with the epiatlas samples.',
                        required=True)

    parser.add_argument('-e', '--epi', action="store",
                        help='The root path to a file with the md5sum from ihec samples that matched with the epiatlas samples.',
                        required=True)

    parser.add_argument('-j', '--fjson', action="store",
                        help='path to the ihec final json',
                        required=True)
    parser.add_argument('-J', '--fJSON', action="store",
                        help='path to the epiatlas final json',
                        required=True)
    
    parser.add_argument('-o', '--output', action="store",
                        help='path to output epiatlas_final_cell_type json',
                        required=True)
    
    
    args = parser.parse_args()

   
    main()
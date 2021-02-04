import json
import sys
import argparse
#from tqdm import tqdm


def cell_type_dset(epi_js):
    list_dset = []
    list_md5 = []
    # ctn = 0
    for dset in epi_js['datasets']:

        if 'cell_type' in dset:
            # ctn += 1

            list_dset.append(dset)
            list_md5.append(dset['md5sum'])
    return list_dset, list_md5


# test = cell_type_dset(epi_js)

def write_json(path, list_dset):
    """Write content to json path"""
    with open(path, 'w') as f:
        json.dump({"datasets":list_dset}, f)

def write_txt(path, list_md5):
    '''write content to txt path'''
    
    with open(path, 'w') as fn:
        for item in list_md5:
            fn.write("%s\n" % item)

def main():


    epi = open(sys.argv[1], 'r') #path to epiatlas json
    path = sys.argv[2] # path to write the filtered json
    path_md5 = sys.argv[3] # path to write the list with the respectives md5sum
    epi_js = json.load(epi)
    list_dset = []
    list_dset, list_md5 = cell_type_dset(epi_js)
    #print(len(list_md5))
    write_json(path, list_dset)
    write_txt(path_md5, list_md5)


if __name__ == "__main__":

    main()
# Work-Json
## Scripts to manipulate the keys and values of several json files

# Requirements
``` python 3 ``` and 
```install tqdm library```

- get_dataset_md5_jsons.py

``` 
Usage: get_dataset_md5_jsons.py [-h] [-p PATH] [-l LIST] [-d DEST]

A script to find in a first moment the dataset name related to a list of
md5sum obtained from a specific assembly/release/IHEC/final json files
(project related with EpiLap).The list of dataset names will be used to
recover the md5sum information in the json files from another assembly/release
(using the final json file)This script returns a txt file with the md5sum
information related to the second assembly release that are inserted in the
first assembly (i.e the md5sum of hg19 that matched in hg38)

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  root path to the final json (for instance
                        hg38-2019-11_final.json) to get the dataset name from
                        a list of md5sum
  -l LIST, --list LIST  root path to a list of md5sum obtained from one
                        IHEC/final assembly-release json. For instance: list
                        of md5sum from hg38.
  -d DEST, --dest DEST  root path to the final json (for instance hg19) to
                        check if the dataset names from hg38 exist
```

- add_celltype_epiatlas.py 

```
usage: add_celtype_epiatlas.py [-h] -i IHEC -e EPI -j FJSON -J FJSON -o OUTPUT

A script to add the cell_type key from the ihec_final json to epiatlas json.

optional arguments:
  -h, --help            show this help message and exit
  -i IHEC, --ihec IHEC  The root path to a file with the md5sum from ihec
                        samples that matched with the epiatlas samples.
  -e EPI, --epi EPI     The root path to a file with the md5sum from ihec
                        samples that matched with the epiatlas samples.
  -j FJSON, --fjson FJSON
                        path to the ihec final json
  -J FJSON, --fJSON FJSON
                        path to the epiatlas final json
  -o OUTPUT, --output OUTPUT
                        path to output epiatlas_final_cell_type json 

```

- filter_pval_json.py


```
usage: filter_pval_json.py [-h] [-p PATH] [-d DSET] [-m MD5]

A script to filter pval and input samples from a json file)

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  root path to the json file
  -d DSET, --dset DSET  root path to write the new json file
  -m MD5, --md5 MD5     root path to write the md5 sum files in a txt file

```


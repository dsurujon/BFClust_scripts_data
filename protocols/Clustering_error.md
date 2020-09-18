## Computing cluster error

### Format output data
First, we need to convert all outputs into the same tabularized format. Use the following scripts to convert each output to a table that contains 2 columns: gene ID (i.e. fasta header) and cluster assignment. 

1. CD-HIT output
Use [this script](https://github.com/dsurujon/BFClust_scripts_data/blob/master/scripts/process_cluster_out.py): 
```
python process_cluster_out.py -i ./CDHIT/synthetic/1e-12.out.clstr -o ./synthetic_tsv/CDHIT_1e-12.tsv
```

2. UClust output
Use the same script with the ```--UC``` flag. 
```
python process_cluster_out.py -i ./UClust/synthetic/1e-12.out -o ./synthetic_tsv/UClust_1e-12.tsv --UC
```

3. Roary output
Use [this script](https://github.com/dsurujon/BFClust_scripts_data/blob/master/scripts/process_roary.py)
```
python ./output/process_roary.py -i ./test/gene_presence_absence.csv -o ./test/testout.tsv
```


4. PanX output
Use [this script](https://github.com/dsurujon/BFClust_scripts_data/blob/master/scripts/process_panX.py)
```
python ./output/process_panX.py -i ./test/allclusters_final.tsv -o ./test/panX_out_test.tsv
```

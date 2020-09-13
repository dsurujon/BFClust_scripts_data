Runtime and Memory tests for all 7 tools      
Only use bowie, 10 processors (if parallelization is allowed)    

* Prepare input files in ```/store/data/Clustering/input```
* Save clustering output in ```/store/data/Clustering/output```
* Record the time and memory in ```/store/data/Clustering/Time_Memory.csv```



## Input data preparation

Different tools use different file formats. You can first copy over the genbank files, and then convert them to GFF and Fasta. 
* panX, BFClust.py: GBK
* UClust, CD-HIT: Fasta
* Roary, PIRATE, Panaroo: GFF3

Use (randomly selected) 25, 50, 100, 150, 200, 250 genomes from the Maela set.     
Copy the gbk files from here: ```/store/home/surujon/GBKs/Chewapreecha/```    
Make one sub-directory for each set (M25, M50, M100, ...) under ```/store/data/Clustering/input/GBK/``` and copy the genomes there.     
Use ```/store/data/Clustering/input/genbank2gff3_Maela.py``` to convert GBK --> GFF3    

As an example, I used a smaller dataset of 5 genomes (M5) for each step below.     

```
mkdir GFF3/M5
python genbank2gff3_Maela.py -i GBK/M5 -o GFF3/M5
```

Use ```/store/data/Clustering/input/make_fasta_fromALLGBKs.py``` to convert GBK --> Fasta
(this assembles all CDS records in all gbk files into a single fasta file)

```
python make_fasta_fromALLGBKs.py -i GBK/M5 -o Fasta/M5.fasta
```

## Running each tool

In order to get run statistics on any command, run it as follows: 
```
/usr/bin/time -v [clustering command]
```
You would probably want to run the slower algorithms on the background so that the run doesn't stop when you disconnect from the server. In order to do this, and to record the run stats, type the following: 
```
nohup /usr/bin/time -v [clustering command] > logfile.txt &
```
(Replace the name of the log file with an appropriate name that contains the dataset and the method.     

Run each of these from ```/store/data/Clustering/```
### CD-HIT
Best to work in a conda environment where cd-hit is already installed e.g. ```pirate_env```. Copy the [pirate_env.yml](https://github.com/dsurujon/BFClust_scripts_data/blob/master/protocols/pirate_env.yml) file into the directory you're in and then run the following to create and actiavte this environment: 
```
conda env create -f pirate_env.yml    
conda activate pirate_env
```

This uses 10 processors, unlimited memory
```
cd-hit -i ./input/Fasta/M5.fasta -o ./output/CDHIT/M5.out -d 0 -n 4 -c 0.7 -G 1 -s 0.7 -g 1 -M 0 -T 10
```

The full command for running it in the background and recording a log would be:     
```
nohup /usr/bin/time -v cd-hit -i ./input/Fasta/M5.fasta -o ./output/CDHIT/M5.out -d 0 -n 4 -c 0.7 -G 1 -s 0.7 -g 1 -M 0 -T 10 > ./output/CDHIT/M5_CDHIT.log &
```

The relevant pieces of information will be "User time (seconds)" and "Maximum resident set size (kbytes)" - record these in the spreadsheet.     

### UCLUST
```
nohup /usr/bin/time -v  /store/home/surujon/UCLUST/usearch11.0 -cluster_fast ./input/Fasta/M5.fasta -id 0.7 -minsl 0.7 -uc ./output/UClust/M5.out > ./output/UClust/M5_UClust.log &
```

### Roary
Use the Roary environment 
```
conda env create -f roary_env.yml    
conda activate roary_env

nohup /usr/bin/time -v roary -f ./output/Roary/M5 -e -n -v input/GFF3/M5/*.gff -p 10 > ./output/Roary/M5_Roary.log &
```

### PanX
Best to run in the ```panX``` environment. Refer to the [PanX documentation](https://github.com/neherlab/pan-genome-analysis#installing-dependencies) for instructions on how to set up the panX environment.     
panX re-arranges the input GBK folder. So copy the GBKs into the output/panX directory and use that for all panX operations
```
mkdir ./output/PanX/M5/
cp ./input/GBK/M5/* ./output/PanX/M5/
conda activate panX
nohup /usr/bin/time -v /store/home/surujon/panX/pan-genome-analysis/panX.py -fn ./output/PanX/M5 -sl M5 -t 10 > ./output/PanX/M5_panX.log &
```

### BFClust.py
You need to run this in a conda environment (requires python 3.6 and some other dependencies). Copy the file [bfclust_env.yml](https://github.com/dsurujon/BFClust_scripts_data/blob/master/protocols/bfclust_env.yml) into your directory. Then create the BFClust environment and activate:  
```
conda env create -f bfclust_env.yml    
conda activate bfclust_env
``` 
*Note: most recent version is 0.1.24 (as of 09/13/20), use the installation instructions on the [BFClust-python repo](https://github.com/dsurujon/BFClust-python) to get the most recent version*     
Then run BFClust (it automatically uses 10 processors) 
```
nohup /usr/bin/time -v  BFC.py -i ./input/GBK/M5/ -o ./output/BFClust/M5 -n 10 -t 0.1 -m 10 > ./output/BFClust/M5_BFClust.log &
```
Note: you will stay in the clustering environment untill you log off or deactivate. Use ```conda deactivate``` to go back to the base environment.     

### PIRATE
This one requires the [pirate_env.yml](https://github.com/dsurujon/BFClust_scripts_data/blob/master/protocols/pirate_env.yml) conda environment
```
conda env create -f pirate_env.yml    
conda activate pirate_env
nohup /usr/bin/time -v PIRATE -i ./input/GFF3/M5 -o ./output/PIRATE/M5 -t 10 > ./ouptut/PIRATE/M5_PIRATE.log &
```

### Panaroo 
Easiest to do on the [panaroo_env](https://github.com/dsurujon/BFClust_scripts_data/blob/master/protocols/panaroo_env.yml) conda environment
```
conda env create -f panaroo_env.yml 
conda activate panaroo_env
nohup /usr/bin/time -v panaroo -i ./input/GFF3/M5/* -o ./output/Panaroo/M5 -t 10 --clean-mode sensitive > ./output/Panaroo/M5_Panaroo.log &
```


Runtime and Memory tests for all 7 tools      
Only use bowie, 10 processors (if parallelization is allowed)    

* Prepare input files in ```/store/data/Clustering/input```
* Save clustering output in ```/store/data/Clustering/output```
* Record the time and memory in ```/store/data/Clustering/Time_Memory.csv```



## Input data preparation

Different tools use different file formats. You can first copy over the genbank files, and then convert them to GFF and Fasta. 
* panX, BFClust.py: GBK
* UClust, CD-HIT: Fasta
R* oary, PIRATE, Panaroo: GFF3

Use (randomly selected) 25, 50, 100, 150, 200, 250 genomes from the Maela set.     
Copy the gbk files from here: ```/store/home/surujon/GBKs/Chewapreecha/```    
Make one sub-directory for each set (M25, M50, M100, ...) under ```/store/data/Clustering/input/GBK/``` and copy the genomes there.     
Use ```/store/data/Clustering/input/genbank2gff3_Maela.py``` to convert GBK --> GFF3    
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

### PIRATE


### Panaroo


### Roary


### PanX


### BFClust.py
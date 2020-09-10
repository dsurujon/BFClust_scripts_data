# BFClust_scripts_data
This directory supplements the BFClust publication by Surujon et al., and includes all custom code and data files. 

## protocols
Set of markdown files as guides to run all pipelines

## scripts
Custom scripts used in any pre/post-processing    
```make_fasta_fromALLGBKs.py```: generates a single fasta file with CDS's from all genbank files in a given directory. The fasta file output contains amino acid sequences.     
```genbank2gff3.py```: converts all gbk files in a given directory into gff3 format, and writes them in a specified output directory     
```panaroo_filter_gff.py```: removes CDS's that have internal stop codons or have nucleotide sequences of a length that's not divisible by 3.    



## data
Data files

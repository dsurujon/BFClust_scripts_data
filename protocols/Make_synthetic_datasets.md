[simurg](https://github.com/iferres/simurg) was used to generate synthetic datasets for benchmarking BFClust against other clustering tools. *E. coli* assembly ASM584v2 was used as the template genome.

The following parameters were held constant:
- ```norg = 10``` (number of sampled organisms)
- ```ne = 1e9``` (number of generations to simulate)
- ```C = 2000``` (size of core genome)
- ```u = 1e-8``` (per-generation gene gain probability)
- ```v = 1e-11``` (per-generation gene loss probability)
- ```replace = FALSE``` (for gene sampling without replacement)

A total of 10 synthetic datasets were generated for each of the following values of ```mu``` (per-site, per-generation nucleotide substitution probability):
- ```1e-12```, ```2e-12```, ```5e-12```, ```1e-11```, ```2e-11```, ```5e-11```, ```1e-10```, ```2e-10```, ```5e-10```, ```1e-9```, ```1e-8```, ```1e-7```

The FASTA files outputted by simurg were annotated and formatted into GBK and GFF3 formats with [Prokka](https://github.com/tseemann/prokka).

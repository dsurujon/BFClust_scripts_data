This document details how to make a synthetic dataset for evaluation of orthologue clustering software.     
This is based on the synthetic dataset generation steps described in the [Panaroo publication](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-020-02090-4).     

*	Start with E. coli ASM584v2
*	Simulate gene gain/loss with [dendropy](https://dendropy.org/) 
*	Use [Mason](https://www.seqan.de/apps/mason/) to include SNPs and generate simulated Illumina reads
*	Assemble simulated reads with [SPADES](https://cab.spbu.ru/software/spades/)
*	Annotate assemblies with [Prokka](https://github.com/tseemann/prokka) or PGAP

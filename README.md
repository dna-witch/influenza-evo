# Viral Evolution
Understanding how and why viruses evolve is crucial to understanding the epidemiology of viral diseases and designing successful antivirals. RNA viruses mutate at high frequencies over short replication periods, quickly acquiring antiviral drug resistance. This project focuses on quantifying and computationally predicting the parameters that drive selection in inter-host viral evolution using machine learning techniques. Viral population genome data from various timepoints will be used to create a database of profile Hidden Markov Models. The goal is to realistically model viral population evolution across different geographic regions, gaining insights into virulence, pathogenicity, and the future evolutionary directions of of newly mutated viral strains.

## Main Questions
+ Can we identify and predict the selective parameters that led a virus to evolve in a certain way? For example, how and why do viral populations evolve distinctly in different countries?
    + Can we use this information to predict possible virus mutations given a set of environmental conditions, simulating viral evolution in a realistic way?
+ How does the impact of these factors differ between species of viruses?

## About the Data
### Viruses used in initial analysis: 
+ Influenza A/H3N2
    + N = sample size where each sample is an CDS nucleotide sequence = 849,899
    + P = approx. number of nucleotides per complete virus ssRNA sequence = 13,500
    + only CDS regions were analyzed (since CDS regions typically have a low mutation rate unless faced with selective pressures)
### Viruses for further analysis:
+ Measles virus:
    + N = sample size where each sample is a CDS nucleotide sequence = 90
    + P = approx. number of nucleotides per ssRNA sequence = 15,894
    + only CDS regions were analyzed

+ Zika virus
    + N = sample size where each sample is a CDS nucleotide sequence = 458
    + P = approx. number of nucleotides per ssRNA sequence = 10,794
    + only CDS regions were analyzed

All viral genome data was collected from [nextstrain](http://www.nextstrain.org/ "nextstrain"), [NCBI Viral Genomes](https://www.ncbi.nlm.nih.gov/genome/viruses/), [ViPR](https://www.viprbrc.org/brc/home.spg?decorator=vipr "Virus Pathogen Resource"), [IRD](https://www.fludb.org/brc/home.spg?decorator=influenza).

## Built With
+ HMMER3 (Python, for Linux)
+ MUSCLE Multiple Sequence Alignment Algorithm
+ MAFFT Multiple Sequence Aligner
+ IRD Sequence Variation (SNP) Tool
+ DEAP (Distributed Evolutionary Algorithms in Python) (Python Library for GAs)
+ PHYLIP (phylogenetics tool for inferring evolutionary trees)
+ I-TASSER Suite (tools for protein structure modeling)

## Authors
+ Shakuntala Mitra

## License
This project is licensed under the GNU GPLv3 License - see the LICENSE.md file for details.

## Acknowledgments
+ Dr. Alexander Franks (research mentor)
+ Jacob Schreiber
+ UCSB CNSI Knot Computing Services
+ UCSB PSTAT RAS Cluster Computing Services

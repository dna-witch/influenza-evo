# Viral Evolution
Understanding how viral populations evolve is crucial to understanding the epidemiology of viral diseases and designing successful antiviral treatments. RNA viruses mutate at high frequencies over short replication periods, quickly acquiring antiviral drug resistance. This project focuses on quantifying parameters that drive selection in inter-host viral evolution and computationally predicting the values of these parameters using machine learning techniques. Viral population genome data from various timepoints will be used to create a database of profile Hidden Markov Models. The goal is to be able to realistically model viral population evolution across different geographic regions to get insights into virulence, pathogenicity, and environmental stability of newly mutated viral strains.

## Main Questions
+ Can we identify the selective parameters that led a virus to evolve in a certain way?
    + Can we computationally predict the quantitative values for these parameters, thus elucidating their impact on viral evolution in a specific environment?
        + Can we use this information to predict possible virus mutations given a set of environmental conditions, simulating viral evolution in a realistic way?
+ What are the differences in mutation rates between viruses?
+ How do viral populations evolve differently between countries?
+ Can we generate potential future mutated virus genomes, simulating viral population evolution in a realistic manner (taking environmental factors into account)?

## About the Data
### Viruses used in initial analysis: 
+ Measles virus:
    + N = sample size where each sample is an RNA sequence = 90
    + P = approx. number of nucleotides per ssRNA sequence = 15,894
    + only complete genome sequences used

+ Zika virus
    + N = sample size where each sample is an RNA sequence = 458
    + P = approx. number of nucleotides per ssRNA sequence = 10,794
    + only complete genome sequences used

+ Influenza A/H3N2
    + N = sample size where each sample is an RNA sequence = 2079
    + P = approx. number of nucleotides per ssRNA sequence = 13,500
    + only complete genome sequences used

All viral genome data was collected from [nextstrain](http://www.nextstrain.org/ "nextstrain"), [NCBI Viral Genomes](https://www.ncbi.nlm.nih.gov/genome/viruses/), and [ViPR](https://www.viprbrc.org/brc/home.spg?decorator=vipr "Virus Pathogen Resource").

## Built With
+ Pomegranate (Python Library)
+ YAHMM (Python Library)
+ HMMER3 (Python, for Linux)

## Authors
+ Shakuntala Mitra

## License
This project is licensed under the GNU GPLv3 License - see the LICENSE.md file for details.

## Acknowledgments
+ Dr. Alexander Franks (research mentor)
+ Jacob Schreiber
+ UCSB CNSI Knot Computing Services

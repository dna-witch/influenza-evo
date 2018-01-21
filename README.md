# Viral Evolution
Understanding how viral populations evolve is crucial to understanding the epidemiology of viral diseases as well as to designing successful antiviral treatments. RNA viruses mutate at high frequencies over short replication periods, quickly acquiring antiviral drug resistance. This project focuses on identifying quantitative parameters that drive selection in inter-host viral evolution and computationally predicting the values of these parameters using machine learning techniques. Viral population genome data will be collected from various times and compared to an original population using Hidden Markov Models. The goal is to be able to model viral sequence evolution, selective pressures, and get insights into virulence, pathogenicity, and environmental stability.

## Main Questions
+ Can we identify the selective parameters that led a virus to evolve in a certain way?
    + Can we computationally predict the quantitative values for these parameters, thus elucidating their impact on viral evolution in a specific environment?
+ What are the differences in mutation rates between viruses?
+ How do viral populations evolve differently between countries?

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
+ Pomegranate (Python Librar)
+ YAHMM (Python Library)

## Authors
+ Shakuntala Mitra

## License
This project is licensed under the GNU GPLv3 License - see the LICENSE.md file for details.

## Acknowledgments
+ Dr. Alexander Franks (research mentor)
+ Jacob Schreiber

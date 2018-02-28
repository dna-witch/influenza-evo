## 2/27/2018
Accomplished:
+ Got HMMER3 to work
+ Collected HPIV Type 4 virus genome data from ViPR
+ Made Multiple Sequence Alignments (MSAs) of virus strains from each continent
+ Built initial profile-HMMs of HPIV Type 4 virus strains across Asia, North America, South America, and Oceania from the MSA files
+ Combined these profile-HMMs to form an initial profile-HMM database called *hpiv4fam*

Next steps:
+ make another HMM database with the protein-coding regions of each virus
  + compare random sequences to the database in an attempt to find commonalities in the CDS's of strains in different countries
  + Possible application of predicting where a strain originated from? Compare results with profile-HMMs of other countries? See which nonstandard proteins arise or which proteins evolve/change most in certain regions over others?
+ use the hmmemit function to generate sample sequences from each profile-HMM (DNA, not protein sequences)
  + try to figure out how to use genetic algorithms to model natural selection and environmental conditions on them
  + This is again to gain insights on which proteins evolve/change most in certain regions over others! By playing with the settings/parameters (in the genetic algorithms), we can see how different factors tend to drive selection in viral populations over time.
  + Selective pressures that are modeled in genetic algorithms must correspond to actual metadata (figure out how to make this work, lol). Want to make the model as realistic as possible!
+ learn how to implement genetic algorithms
+ gather and organize relevant virus + environmental metadata

## 2/28/2018

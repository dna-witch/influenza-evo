# import all necessary libraries
from pomegranate import *
from os import *

# define your model
model = HiddenMarkovModel()

# define your states and do the model.add_states()
# also figure out how to add point mutation states (AC->GT, AC->TG, etc. kind of mutations)

# distribution for insertions; may be more than one! play with this, too
i_d = DiscreteDistribution({'A': 0.25, 'C': 0.25, 'G': 0.25, 'T': 0.25})
# create some insert states
i0 = State(i_d, name="i0")
i1 = State(i_d, name="i1")
i2 = State(i_d, name="i2")
i3 = State(i_d, name="i3")

# create some match states; idk if it matters what these start out as, because you're gonna fit the model, anyway
m1 = State(DiscreteDistribution({'A': 0.95, 'C': 0.01, 'G': 0.01, 'T': 0.02}), name = "m1")
m2 = State(DiscreteDistribution({'A': 0.01, 'C': 0.95, 'G': 0.02, 'T': 0.02}), name = "m2")
m3 = State(DiscreteDistribution({'A': 0.003, 'C': 0.002, 'G': 0.99, 'T': 0.005}), name = "m3")
m4 = State(DiscreteDistribution({'A': 0.01, 'C': 0.01, 'G': 0.01, 'T': 0.97}), name = "m4")

# create some delete states
d1 = State(None, name = "d1")
d2 = State(None, name = "d2")
d3 = State(None, name = "d3")

# Add all states to the model
model.add_states([i0, i1, i2, i3, m1, m2, m3, m4, d1, d2, d3])

# open sample data as a list of sequences

seqNames = ['practiceSeq1.txt', 'practiceSeq2.txt', 'practiceSeq3.txt'] # add in actual filenames
for i in seqNames:
    with open(i, 'r') as seq:
        seqData = list(seq)
        
# fit your model with Baum-Welch training algorithm
model.fit(seqData, algorithm = 'baum-welch')

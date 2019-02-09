#### try the CMA-ES thing lol
### test out the fitness of each virus, so max/min each of the proteins
### start with main 2 proteins (HA, NA), then work up to 8 proteins

# create types (fitness, individual)
import array
import random

from deap import base, creator, tools

creator.create("FitnessMulti", base.Fitness, weights=(-1.0, 1.0))
# weights can be any real number; sign determines if min or max

# Inheriting from Numpy: https://deap.readthedocs.io/en/master/tutorials/advanced/numpy.html
# Evolution strategies individuals contain generally two lists, one for actual individual and one for its mutation parameters
creator.create("Individual", array.array, typecode="d", fitness=creator.FitnessMin, strategy=None)
creator.create("Strategy", array.array, typecode="d")

def initES(icls, scls, size, imin, imax, smin, smax):
    ind = icls(random.uniform(imin, imax) for _ in range(size))
    ind.strategy = scls(random.uniform(smin, smax) for _ in range(size))
    return ind

IND_SIZE = 50 # how does changing this affect outcomes?
MIN_VALUE, MAX_VALUE = -5., 5. # play with this
MIN_STRAT, MAX_STRAT = -1., 1. # play with this too

toolbox = base.Toolbox()
toolbox.register("individual", initES, creator.Individual, creator.Strategy, IND_SIZE, MIN_VALUE, MAX_VALUE, MIN_STRAT, MAX_STRAT)

toolbox.individual()

# attributes? populations?
toolbox.register("individual", tools.initRepeat, creator.Individual,
                 toolbox.attribute, n=IND_SIZE)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# create operators! mate, mutate, select, evaluate (makes sure this makes sense for the problem with CMA-ES algorithm)
def evaluate(individual):
    return sum(individual),

toolbox.register("mate", tools.cxESTwoPoint) # play with cxESTwoPoint and cxESBlend
toolbox.regis("mutate", tools.mutES, mu=0, sigma=1, indpb=0.1) # play with mutation scheme; double check for errors
toolbox.register("select", tools.selTournament, tournsize=8) # play with tournsize
toolbox.register("evaluate", evaluate)

# now everything we need to write the algorithm has been created! let's write the main function

# main function
def main():
    pop = toolbox.population(n=100)
    CXPB, MUTPB, NGEN = 0.5, 0.2, 40 # crossover prob, mutation prob, and number of generations

    # Evaluate the entire population
    # write some shit here


    for g in range(NGEN):
        # select next generation individuals (don't just select the best, make sure to take some randomly)
        # Clone the selected individuals (offspring)

        # apply crossover and mutations on the offspring


        # evaluate the individuals w/ an invalid fitness

        # the population is entirely replaced by the new offspring
        pop[:] = offspring

    return pop

##### check out other algorithms and their variations to build your own: https://deap.readthedocs.io/en/master/api/algo.html#module-deap.algorithms

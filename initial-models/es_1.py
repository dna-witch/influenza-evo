#### try the CMA-ES thing lol
### test out the fitness of each virus, so max/min each of the proteins
### start with main 2 proteins (HA, NA), then work up to 8 proteins

# create types (fitness, individual)
import array
import random

from deap import base, creator, tools, algorithms, benchmarks, cma
from deap.benchmarks.tools import hypervolume

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
toolbox.register("mutate", tools.mutES, mu=0, sigma=1, indpb=0.1) # play with mutation scheme; double check for errors
toolbox.register("select", tools.selTournament, tournsize=8) # play with tournsize
toolbox.register("evaluate", evaluate)

# now everything we need to write the algorithm has been created! let's write the main function

# main function
def main():
    population = [creator.Individual(x) for x in (numpy.random.uniform(0, 1, (MU, N)))]
    CXPB, MUTPB, NGEN = 0.5, 0.2, 40 # crossover prob, mutation prob, and number of generations

    for ind in population:
        ind.fitness.values = toolbox.evaluate(ind)

    strategy = cma.StrategyMultiObjective(population, sigma=1.0, mu=MU, lambda_=LAMBDA)
    toolbox.register("generate", strategy.generate, creator.Individual)
    toolbox.register("update", strategy.update)

    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("min", numpy.min, axis=0)
    stats.register("max", numpy.max, axis=0)

    logbook = tools.Logbook()
    logbook.header = ["gen", "nevals"] + (stats.fields if stats else [])

    fitness_history = []

    for g in range(NGEN):
        # select next generation individuals (don't just select the best, make sure to take some randomly)
        # Clone the selected individuals (offspring)
        population = toolbox.generate()

        # apply crossover and mutations on the offspring


        # evaluate the individuals w/ an invalid fitness
        fitnesses = toolbox.map(toolbox.evaluate, population)
        for ind, fit in zip(population, fitnesses):
            ind.fitness.values = fit
            fitness_history.append(fit)

        # the population is entirely replaced by the new offspring
        toolbox.update(population)


        record = stats.compile(population) if stats is not None else {}
        logbook.record(gen=gen, nevals=len(population), **record)
        if verbose:
            print(logbook.stream)

    if verbose:
        print("Final population hypervolume is %f" % hypervolume(strategy.parents, [11.0, 11.0]))

        # Note that we use a penalty to guide the search to feasible solutions,
        # but there is no guarantee that individuals are valid.
        # We expect the best individuals will be within bounds or very close.
        num_valid = 0
        for ind in strategy.parents:
            dist = distance(closest_feasible(ind), ind)
            if numpy.isclose(dist, 0.0, rtol=1.e-5, atol=1.e-5):
                num_valid += 1
        print("Number of valid individuals is %d/%d" % (num_valid, len(strategy.parents)))

        print("Final population:")
        print(numpy.asarray(strategy.parents))

      if create_plot:
        interactive = 0
        if not interactive:
            import matplotlib as mpl_tmp
            mpl_tmp.use('Agg')   # Force matplotlib to not use any Xwindows backend.
        import matplotlib.pyplot as plt

        fig = plt.figure()
        plt.title("Multi-objective minimization via MO-CMA-ES")
        plt.xlabel("First objective (function) to minimize")
        plt.ylabel("Second objective (function) to minimize")

        # Limit the scale because our history values include the penalty.
        plt.xlim((-0.1, 1.20))
        plt.ylim((-0.1, 1.20))

        # Plot all history. Note the values include the penalty.
        fitness_history = numpy.asarray(fitness_history)
        plt.scatter(fitness_history[:,0], fitness_history[:,1],
            facecolors='none', edgecolors="lightblue")

        valid_front = numpy.array([ind.fitness.values for ind in strategy.parents if close_valid(ind)])
        invalid_front = numpy.array([ind.fitness.values for ind in strategy.parents if not close_valid(ind)])

        if len(valid_front) > 0:
            plt.scatter(valid_front[:,0], valid_front[:,1], c="g")
        if len(invalid_front) > 0:
            plt.scatter(invalid_front[:,0], invalid_front[:,1], c="r")

        if interactive:
            plt.show()
        else:
            print("Writing cma_mo.png")
            plt.savefig("cma_mo.png")

    return strategy.parents

if __name__ == "__main__":
    solutions = main()
#    return population


##### check out other algorithms and their variations to build your own: https://deap.readthedocs.io/en/master/api/algo.html#module-deap.algorithms

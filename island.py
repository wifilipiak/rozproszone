# -*- coding: utf-8 -*-
"""

"""
import random
import threading
from result import AlgResult
from params import AlgParams
from deap import algorithms
from deap import base
from deap import creator
from deap import tools


def evalTSP(individual, distance_map):
    distance = distance_map[individual[-1]][individual[0]]
    for gene1, gene2 in zip(individual[0:-1], individual[1:]):
        distance += distance_map[gene1][gene2]
    return distance,


class Island(threading.Thread):
    def __init__(self, id, json_data, q_in, q_out):
        super(Island, self).__init__()
        self.id = id
        self.alg_params = AlgParams()
        self.iterations = self.alg_params.iterations
        self.pop_size = self.alg_params.pop_size
        self.results = AlgResult(self.id)
        self.json_data = json_data
        self.q_in = q_in
        self.q_out = q_out

        IND_SIZE = json_data["TourSize"]

        self.distance_map = json_data["DistanceMatrix"]
        self.toolbox = base.Toolbox()
        # Attribute generator
        self.toolbox.register("indices", random.sample, range(IND_SIZE), IND_SIZE)
        # Structure initializers
        self.toolbox.register("individual", tools.initIterate, creator.Individual, self.toolbox.indices)
        self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)
        # Add methods to toolbox
        self.toolbox.register("mate", self.alg_params.mating_method)
        self.toolbox.register("mutate", self.alg_params.mutation_method, indpb=self.alg_params.shuffle_probability)
        self.toolbox.register("select", self.alg_params.selection_method, tournsize=self.alg_params.selection_size)
        self.toolbox.register("evaluate", evalTSP, distance_map=self.distance_map)
        # Init random numbers generator with given seed (used in population generator)
        random.seed(111)
        # Create population - list of Individual objects
        self.population = self.toolbox.population(n=self.pop_size)
        # Evaluate population
        for ind in self.population:
            ind.fitness.values = self.toolbox.evaluate(ind)

    def migrate(self):
        # Send your emigrants to queue_out and replace random individuals with immigrants from queue_in
        emigrants = tools.selBest(self.population, self.alg_params.migration_size)
        self.q_out.put(emigrants)
        buf = self.q_in.get(block=True)
        replacements = random.sample(self.population, len(buf))
        for i in range(len(buf)):
            index = self.population.index(replacements[i])
            self.population[index] = buf[i]

    def start_optimization(self):
        for i in range(1, self.alg_params.iterations):
            self.population = algorithms.varAnd(self.population, self.toolbox, self.alg_params.mating_probability
                                                , self.alg_params.mutation_probability)
            invalid_ind = [ind for ind in self.population if not ind.fitness.valid]
            for ind in invalid_ind:
                ind.fitness.values = self.toolbox.evaluate(ind)
            self.update_results()
            if i % self.alg_params.migration_rate == 0 and i > 0:
                self.migrate()
        print(f'Island {self.id} done\n')

    def update_results(self):
        self.results.update(self.population)



  
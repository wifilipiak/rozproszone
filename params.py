# -*- coding: utf-8 -*-
"""
parameters of genetic algorithm on certain island
"""
from deap import tools
import random


class AlgParams:
    def __init__(self):
        self.pop_size = 200
        self.iterations = 500
        self.mating_probability = round(random.uniform(0, 1), 2)                   #original = 0.7
        self.mating_method = tools.cxPartialyMatched
        self.mutation_probability = round(random.uniform(0, 1), 2)                #original = 0.3
        self.shuffle_probability = round(random.uniform(0, 0.2), 3)     #original = 0.05
        self.mutation_method = tools.mutShuffleIndexes
        self.selection_size = random.randint(2, 10)              #original = 3
        self.selection_method = tools.selTournament
        self.migration_rate = 20
        self.migration_size = 10

    def get_params(self):
        params = {'Mating': self.mating_probability, 'Mutation': self.mutation_probability,
                  'Shuffle': self.shuffle_probability, 'Selection': self.selection_size}
        return params

    def set_params(self, params):
        self.mating_probability = params['Mating']
        self.mutation_probability = params['Mutation']
        self.shuffle_probability = params['Shuffle']
        self.selection_size = params['Selection']

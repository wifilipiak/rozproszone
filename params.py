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
        self.mating_probability = random.uniform(0.3, 0.8)                   #original = 0.7
        self.mating_method = tools.cxPartialyMatched
        self.mutation_probability = random.uniform(0.1, 0.6)                #original = 0.3
        self.shuffle_probability = random.uniform(0.03, 0.1)     #original = 0.05
        self.mutation_method = tools.mutShuffleIndexes
        self.selection_size = random.randint(3, 10)              #original = 3
        self.selection_method = tools.selTournament
        self.migration_rate = 20
        self.migration_size = 10


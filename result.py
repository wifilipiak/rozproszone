# -*- coding: utf-8 -*-
"""

"""
from deap import tools
import numpy

class AlgResult():
    def __init__(self, island_id):
        self.island_id = island_id
        self.best_route = []
        # Create HallOfFame object to keep the best Individual
        self.hof = tools.HallOfFame(1)
        # Create statistics object and add functions to apply
        self.stats = tools.Statistics(lambda ind: ind.fitness.values)
        self.stats.register("avg", numpy.mean)
        self.stats.register("std", numpy.std)
        self.stats.register("min", numpy.min)
        self.stats.register("max", numpy.max)
        
    def update(self, population):
        # Check if not empty
        if population:
            self.hof.update(population)
            # Run registered functions on pop
            self.stats.compile(population)
            self.best_route = self.hof[0].tolist()
            #[x + 1 for x in self.hof[0].tolist()]
        else:
            pass

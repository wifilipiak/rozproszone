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
            # Change route format from <0,28> to <1,29> to match with json file
            self.best_route = [x + 1 for x in self.hof[0].tolist()]
        else:
            pass

# -*- coding: utf-8 -*-
"""

"""
import random
import threading
from TSP_GA import Algorithm
from result import AlgResult
from params import AlgParams

class Island(threading.Thread):
    def __init__(self,id):
        super(Island, self).__init__()
        self.algorithm = Algorithm
        self.population = []
        self.results = AlgResult()
        self.alg_params = AlgParams()
        self.id = id
        
    def get_population(self):
        self.population = Algorithm.pop
    
    def start_optimization(self):
        self.algorithm.start()
    
    def get_hierarchy(self):
        self.results.best = self.algorithm.hierarchy[0]
        self.results.best_goal_value = self.algorithm.hierarchy[0]
        self.results.for_migration = self.algorithm.hierarchy[0:9]
        
    def take_migrants(self):
        for i in range (10):
            random_item_from_list = random.choice(self.population)
            self.population.remove(random_item_from_list)
        




  
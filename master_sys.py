# -*- coding: utf-8 -*-
"""

"""

import random
import threading
from TSP_GA import Algorithm
from result import AlgResult
from params import AlgParams
from island import Island

class Master(threading.Thread):
    def __init__(self,period=20,max_iter=500,goal_bound=20,num_of_islands=12):
        super(Master, self).__init__()
        self.period = period
        self.iteration = 0
        self.islands_list = []
        self.best_results_list = []
        self.best_global_result = AlgResult()
        self.max_iter = []
        self.accepted_goal_bound = goal_bound
        self.num_of_islands = num_of_islands
        self.alg_params = AlgParams()
        
    def set_up(self,**params):
        for i in range(num_of_islands):
            self.islands_list.append(Island(i))
        ...
        
    def stop_all(self):
        
    
    def clear_all(self):
        
        
    def get_and_compare_alg_results(self):
        
            
    def get_best_migrant(self):
        
        
    def send_migrant(self):
        
            

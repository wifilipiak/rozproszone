# -*- coding: utf-8 -*-
"""
parameters of genetic algorithm on certain island
"""

class AlgParams():
    def __init__(self,num_parents, mutation_rate, mutation,crossing):
        self.num_of_selected_parents = num_parents
        self.crossing_method = crossing
        self.mutation_rate = mutation_rate
        self.mutation_method = mutation
# -*- coding: utf-8 -*-
"""

"""

import threading
import queue
import json
import array
from deap import base
from deap import creator
from island import Island
with open("bays29.json", "r") as tsp_data:
    json_data = json.load(tsp_data)


class Master(threading.Thread):
    def __init__(self, goal_bound=20, num_of_islands=12):
        super(Master, self).__init__()
        self.islands_list = []
        self.queues_list = []
        self.threads_list = []
        self.results = []
        self.accepted_goal_bound = goal_bound
        self.num_of_islands = num_of_islands
        # Create classes
        creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
        creator.create("Individual", array.array, typecode='i', fitness=creator.FitnessMin)
        
    def set_up(self,**params):
        for i in range(self.num_of_islands):
            self.queues_list.append(queue.Queue(maxsize=0))
        for i in range(self.num_of_islands):
            self.islands_list.append(Island(i, json_data, self.queues_list[i-1], self.queues_list[i]))
            thread = threading.Thread(target=self.islands_list[i].start_optimization)
            self.threads_list.append(thread)

    def start_all(self):
        for thread in self.threads_list:
            thread.start()

    def join_all(self):
        for thread in self.threads_list:
            thread.join()

    def get_results(self):
        for island in self.islands_list:
            self.results.append({'Route' : island.results.best_route, 'Value': island.results.hof[0].fitness.values[0]})
        print(self.results)
        return min(self.results, key= lambda x: x['Value'])


if __name__ == "__main__":
    master = Master()
    master.set_up()
    master.start_all()
    master.join_all()
    print(master.get_results())




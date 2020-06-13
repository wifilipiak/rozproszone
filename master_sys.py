# -*- coding: utf-8 -*-
"""

"""

import threading
import queue
import json
import array
import matplotlib.pyplot as plt
from deap import base
from deap import creator
from island import Island
with open("bays29.json", "r") as tsp_data:
    json_data = json.load(tsp_data)


class Master(threading.Thread):
    def __init__(self, goal_bound=20, num_of_islands=15):
        super(Master, self).__init__()
        self.islands_list = []
        self.queues_list = []
        self.threads_list = []
        self.best = {}
        self.accepted_goal_bound = goal_bound
        self.num_of_islands = num_of_islands
        # Create classes
        creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
        creator.create("Individual", array.array, typecode='i', fitness=creator.FitnessMin)
        
    def set_up(self, **params):
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
        results = []
        for island in self.islands_list:
            results.append({'Route': island.results.best_route, 'Value': island.results.hof[0].fitness.values[0]})
        self.best = min(results, key=lambda x: x['Value'])
        return self.best

    def plot_results(self):
        points = json_data["Display data"]
        xs = [x[1] for x in points]
        ys = [y[2] for y in points]
        optimal_tour = [x - 1 for x in json_data["OptTour"]]
        fig, ax = plt.subplots(2, sharex=True, sharey=True)
        ax[0].set_title('Our route')
        ax[1].set_title('Best known route')
        ax[0].scatter(xs, ys)
        ax[1].scatter(xs, ys)
        text_our = f'Route: {[x + 1 for x in self.best["Route"]]} \nLength: {self.best["Value"]}'
        text_opt = f'Route: {json_data["OptTour"]} \nLength: {json_data["OptDistance"]}'
        plt.subplots_adjust(hspace=0.5)
        plt.gcf().text(0.25, 0.5, text_our, fontsize=12)
        plt.gcf().text(0.25, 0.03, text_opt, fontsize=12)
        for i in range(len(self.best['Route'])):
            start = (points[self.best['Route'][i-1]][1], points[self.best['Route'][i-1]][2])
            end = (points[self.best['Route'][i]][1], points[self.best['Route'][i]][2])
            ax[0].annotate("", end, start,arrowprops=dict(arrowstyle="->"))
        ax[0].scatter(points[self.best['Route'][0]][1], points[self.best['Route'][0]][2])
        for i in range(len(self.best['Route'])):
            start = (points[optimal_tour[i-1]][1], points[optimal_tour[i-1]][2])
            end = (points[optimal_tour[i]][1], points[optimal_tour[i]][2])
            ax[1].annotate("", end, start,arrowprops=dict(arrowstyle="->"))
        ax[1].scatter(points[optimal_tour[0]][1], points[optimal_tour[0]][2])
        plt.show()


if __name__ == "__main__":
    master = Master()
    master.set_up()
    master.start_all()
    master.join_all()
    print(master.get_results())
    master.plot_results()





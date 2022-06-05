import random 
import numpy as np
import sys
from py2opt.routefinder import RouteFinder

def OPT(graph, city_names):
    route_finder = RouteFinder(graph, city_names, iterations=1)
    min_distance, best_path = route_finder.solve()
    return best_path

def calculate_cost(graph,cities):
    cost = 0
    for i in range(1,cities.len(cities)):
        cost += graph[cities[i]][cities[i - 1]]
    return cost;

# def calculate_Hamming_dist(x,xbest):
#         dist = 0
#         for i in range(x.len):
#             dist += abs(x[i] - xbest[i])
#         return dist
    
class BatAlgorithm_tsp():
    def __init__(self, num_bats, t, r, A,cities,graph):
        self.num_bats = num_bats  #population of bats
        self.t= t  #giterations
        self.r = r  #pulse rate
        self.A = A  #loudness
        self.cities = cities #permutation of cities
        self.graph = graph #cost matrix 

    def solve(self):
        city_temp = OPT(self.cities,self.graph)
        # v = calculate_Hamming_dist(city_temp,xbest)
        # v =  np.random.uniform(1, v)
        cost = calculate_cost(city_temp)
        return [cost,city_temp]



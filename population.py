# population.py

import math
import random
import cannon

# Defines a population of cannons to be evolved
class Population:
    population = []
    def __init__(self, n, x, y):
        self.population = [cannon.Cannon(x, y) for i in range(0, n)]
    
    def getStats(self):
        stats = []
        for cannon in self.population:
            stats.append(cannon.getStats())
        return stats
    
    def getVelocity(self):
        velocities = []
        for cannon in self.population:
            velocities.append(cannon.getVelocity())

population = Population(100, 0, 0)
print(population.getStats())
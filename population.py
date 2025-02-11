# population.py

import math
import random
import cannon

# Defines a population of cannons to be evolved, mimics many cannon function but as a group
class Population:
    population = [] # list of cannons

    # Init a new population from scratch
    def __init__(self, n=100, x=0, y=0, existingPopulation=None):
        random.seed()
        if existingPopulation is None:
            self.population = [cannon.Cannon(x, y) for i in range(0, n)]
        else:
            self.population = existingPopulation
    
    # Fire all cannons and get the coordinates of each at time t
    def fire(self, t: float):
        return [cannon.fire(t) for cannon in self.getPop()]
    
    # Kill a percent of the total population randomly.
    def cull(self, percent):
        # Check that percent is valid
        if percent > 100 or percent < 0:
            return 0
        
        # Calculate total num of cannons to be removed
        num = int(self.size() * percent / 100)
        for i in range(0, num):
            # Pick a random index from population
            victim = random.randrange(0, self.size())
            self.getPop().pop(victim)   # Pop vitcim from population
        
        return num

    # Mutate n characters in both tilt and power gene for all cannons
    def mutateAll(self, n):
        for cannon in self.population:
            cannon.mutateAll(n)

    def mutateTilt(self, n):
        for cannon in self.population:
            cannon.mutateTilt(n)

    def mutatePower(self, n):
        for cannon in self.population:
            cannon.mutatePower(n)

    def copy(self):
        return [cannon.copy() for cannon in self.getPop()]

    def size(self):
        return len(self.getPop())

    # Get a list of all cannon entities in population.
    def getPop(self):
        return self.population

    # Get all tilt genes.
    def getTiltGenes(self):
        return [cannon.getTiltGene() for cannon in self.getPop()]
    
    # Get all power genes.
    def getPowerGenes(self):
        return [cannon.getPowerGene() for cannon in self.getPop()]

    # Get the tilt and power of all cannons.
    def getStats(self):
        return [cannon.getStats() for cannon in self.getPop()]
    
    # Get the x and y velocities of all cannons.
    def getVelocities(self):
        return [cannon.getVelocity() for cannon in self.getPop()]
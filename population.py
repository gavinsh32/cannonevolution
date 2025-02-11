# population.py

import math
import random
import cannon

# Defines a list of cannons, and extends cannon functionality to work on a population
class Population:
    population = [] # list of cannons

    # Init a new population from scratch
    def __init__(self, n=100, x=0, y=0, existing=None):
        random.seed()
        if existing is None:
            self.population = [cannon.Cannon(x, y) for i in range(0, n)]
        else:
            self.setPop(existing)
    
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

    # Mutate at most n characters in each tilt gene
    def mutateTilt(self, n):
        for cannon in self.population:
            cannon.mutateTilt(n)

    # Mutate at most n characters in each power gene
    def mutatePower(self, n):
        for cannon in self.population:
            cannon.mutatePower(n)

    # Mutate n characters in both tilt and power gene for all cannons
    def mutateAll(self, n):
        for cannon in self.population:
            cannon.mutateAll(n)

    # Return a copy of the population
    def copy(self):
        return [cannon.copy() for cannon in self.getPop()]

    # Return the length of the population
    def size(self):
        return len(self.getPop())

    # Get a list of all cannon entities in population.
    def getPop(self):
        return self.population
    
    # Set the population to the new list of cannons
    def setPop(self, newPopulation):
        self.population = newPopulation

    def at(self, index) -> cannon:
        if 0 <= index and index < self.size():
            return self.population[index].copy()
        else:
            return None

    def append(self, population):
        if population is not None:
            self.setPop(self.getPop() + population.getPop())

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
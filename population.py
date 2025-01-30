# population.py

import math
import random
import cannon

# Defines a population of cannons to be evolved, mimics many cannon function but as a group
class Population:
    population = [] # list of cannons

    # Init a new population from scratch
    def __init__(self, existingPopulation=[], n=100, x=0, y=0):
        random.seed()
        if len(existingPopulation) < 1:
            self.population = [cannon.Cannon(x, y) for i in range(0, n)]
        else:
            self.population = existingPopulation
    
    # Fire all cannons and get the coordinates of each at time t
    def fire(self, t: float):
        coords = []
        for cannon in self.population:
            coords.append(cannon.fire(t))
        return coords
    
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

    # Get a list of all cannon entities in population.
    def toList(self):
        return self.population

    # Get all tilt genes.
    def getTiltGenes(self):
        tiltGenes = []
        for cannon in self.population:
            tiltGenes.append(cannon.getTiltGene())
        return tiltGenes
    
    # Get all power genes.
    def getPowerGenes(self):
        powerGenes = []
        for cannon in self.population:
            powerGenes.append(cannon.getTiltGene())
        return powerGenes

    # Get the tilt and power of all cannons.
    def getStats(self):
        stats = []
        for cannon in self.population:
            stats.append(cannon.getStats())
        return stats
    
    # Get the x and y velocities of all cannons.
    def getVelocities(self):
        velocities = []
        for cannon in self.population:
            velocities.append(cannon.getVelocity())
        return velocities
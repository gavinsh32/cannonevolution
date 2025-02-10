# population.py

import math
import random
import cannon

# Defines a population of cannons to be evolved, mimics many cannon function but as a group
popSize = 100
class Population:
    population = [] # list of cannons

    # Init a new population from scratch
    def __init__(self, existingPopulation=[], n=100, x=0, y=0):
        random.seed()
        if len(existingPopulation) < 1:
            self.population = [cannon.Cannon(x, y) for i in range(0, n)]
        else:
            self.population = existingPopulation

        self.bestFit = 0 # best fitness
        self.best = 0 # index of best individual
        self.avgFit = 0
        self.calcStats()
        

    def generation(self):
        tempPop = Population()
        for i in range(0, popSize, 2):
            p1 = Population()
            p2 = Population()
            tempPop.population[i].copy(self.population[p1])
            tempPop.population[i+1].copy(self.population[p2])
            tempPop.population[i].crossoverAll(tempPop.population[i+1])
            tempPop.population[i].mutateAll()
            tempPop.population[i+1].mutateAll()
        for i in range(0,popSize):
            self.population[i].copy(tempPop.population[i])

    def tourn(self):
        best = random.randint(0,popSize-1) # the winner so far
        bestfit = self.population[0].fitness # best fit so far
        for i in range(5): # tournament size of 6!!!!
            p2 = random.randint(0,popSize-1)
            if(self.population[p2].fitness > bestfit):
                bestfit = self.population[p2].fitness
                best = p2
        return best

    def calcStats(self):
        self.avgFit = 0
        self.population[0].calcStats()
        self.bestFit = self.population[0].fitness
        self.best = 0
        for i in range(len(self.population)):
            self.population[i].calcStats() # update fitnesses
            if(self.population[i].fitness > self.bestFit): # compare fitness to best
                self.bestFit = self.population[i].fitness
                self.best = i
            self.avgFit += self.population[i].fitness
        self.avgFit = self.avgFit/len(self.population)

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
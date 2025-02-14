# population.py
import math
import random
import cannon

#from main import psize
psize = 1000

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
            
        self.bestFit = 0 # best fitness
        self.best = 0 # index of best individual
        self.avgFit = 0
    
    # Fire all cannons and get the coordinates of each at time t
    def fire(self, t: float):
        return [cannon.fire(t) for cannon in self.getPop()]
    
    # Kill a percent of the total population randomly.
    def cull(self, percent: int) -> None:
        for i in range(0, self.percent(percent)):
            # Pick a random index from population
            victim = random.randrange(0, self.size())
            self.getPop().pop(victim)   # Pop vitcim from population

    # Mutate at most n characters in each tilt gene
    def mutateTilt(self, n: int, per: int) -> None:
        for i in range(0, self.percent(per)):
            random.choice(self.getPop()).mutateTilt(n)

    # Mutate at most n characters in each power gene
    def mutatePower(self, n: int, per: int) -> None:
        for i in range(0, self.percent(per)):
            random.choice(self.getPop()).mutatePower(n)

    # Return a percent of the population size.
    def percent(self, per: int) -> int:
        if 0 <= per and per <= 100:
            return int(self.size() * per / 100)
        else:
            return 0

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
        self.population = newPopulation.getPop()

    # Return a reference to a cannon at an index
    def at(self, index) -> cannon:
        if 0 <= index and index < self.size():
            return self.population[index]
        else:
            return None

    # Reproduce population by a percent, and return children
    def reproduce(self, per):        
        children = Population(0)
        for i in range(0, self.percent(per)):
            child = random.choice(self.getPop())
            children.append(child)

        return Population(existing=children)

    # Join this population with another
    # def join(self, population):
    #     if population is not None:
    #         self.setPop(self.getPop() + population.getPop())
    def join(self, population):
        if population is not None:
            self.population.extend(population.getPop())  

    def append(self, cannon: cannon):
        if cannon is not None:
            self.getPop().append(cannon)

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

    # def generation(self):
    #     tempPop = Population()
    #     for i in range(0, psize, 2):
    #         p1 = Population()
    #         p2 = Population()
    #         tempPop.population[i].copy(self.population[p1])
    #         tempPop.population[i+1].copy(self.population[p2])
    #         tempPop.population[i].crossoverAll(tempPop.population[i+1])
    #         tempPop.population[i].mutateAll()
    #         tempPop.population[i+1].mutateAll()
    #     for i in range(0,psize):
    #         self.population[i].copy(tempPop.population[i])

    # def tourn(self):
    #     best = random.randint(0,psize-1) # the winner so far
    #     bestfit = self.population[0].fitness # best fit so far
    #     for i in range(5): # tournament size of 6!!!!
    #         p2 = random.randint(0,psize-1)
    #         if(self.population[p2].fitness > bestfit):
    #             bestfit = self.population[p2].fitness
    #             best = p2
    #     return best

    # def calcStats(self):
    #     self.avgFit = 0
    #     self.population[0].calcStats()
    #     self.bestFit = self.population[0].fitness
    #     self.best = 0
    #     for i in range(len(self.population)):
    #         self.population[i].calcStats() # update fitnesses
    #         if(self.population[i].fitness > self.bestFit): # compare fitness to best
    #             self.bestFit = self.population[i].fitness
    #             self.best = i
    #         self.avgFit += self.population[i].fitness
    #     self.avgFit = self.avgFit/len(self.population)
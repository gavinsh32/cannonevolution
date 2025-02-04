# simulator.py
# Handles the environment where cannons "shoot"

import population
import cannon
import math
import random

class Simulator:
    population = []
    target = (0, 0, 0, 0)
    dimensions = (100, 100)

    # Init a simulation environment with a population of cannons
    def __init__(self, n=100, x=0, y=0):
        self.population = [cannon.Cannon(x, y) for i in range(0, n)]

    # Init a square target from the bottom left corner
    def initTarget(self, x1, y1, w):
        self.target = (x1, y1, x1 + w, y1 + w)

    # Init dimensions of simulator
    def initBounds(self, w, h):
        self.dimensions = (w, h)

    # Set to a new list of cannons
    def setPopulation(self, newPop):
        self.population = newPop

    # Fire all cannons, checking each step until all projectiles have either hit the target or fallen out of bounds
    def fire(self, step=0.1, max=3):
        hitTarget = []
        hitBounds = []
        t = 0.0
        # While there are still cannons, remove if hit target or bounds
        while len(self.population) > 0:
            # Fire each cannon each time step
            for cannon in self.population:
                result = cannon.fire(t)
                if self.inTarget(result):   # Hit target
                    hitTarget.append(cannon)
                    self.population.remove(cannon)
                if not self.inBounds(result):
                    #print('Hit bounds at', result)
                    hitBounds.append(cannon)
                    self.population.remove(cannon)
            t += step
        return hitTarget, hitBounds, t
    
    # Clone cannons in current population
    def reproduce(self, n, a, b):
        parents = self.copyPop()
        children = []
        for parent in parents:
            for i in range(0, random.randint(0, n)):
                child = parent.copy()
                child.mutatePower(a)
                child.mutateTilt(b)
                children.append(child)
                parents.append(child)
        self.setPopulation(parents)

    def copyPop(self):
        temp = []
        for cannon in self.getPopulation():
            temp.append(cannon.copy())
        return temp

    # Mutate n characters in both tilt and power gene for all cannons
    def mutateAll(self, n):
        for cannon in self.population:
            cannon.mutateTilt(n)
            cannon.mutatePower(n)

    # Mutate randomly between 0 to n genes in each cannon in population
    def mutateTilt(self, n):
        for cannon in self.population:
            cannon.mutateTilt(n)

    def mutatePower(self, n):
        for cannon in self.population:
            cannon.mutatePower(n)

    # Get population (list of cannons)
    def getPopulation(self):
        return self.population

    # Check if the projectile is in the target
    def inTarget(self, coord):
        x, y = coord
        x0, y0, x1, y1 = self.target
        return x > x0 and x < x1 and y > y0 and y < y1

    # Check if a coordinate is in bounds
    def inBounds(self, coord):
        x, y = coord
        w, h = self.dimensions
        return x >= 0 and x <= w and y >= 0 and y <= h

    # Snap a coordinate to simulator bounds
    def snapToBounds(self, coord):
        x, y = coord
        w, h = self.dimensions
        if x < 0: x = 0
        if x > w: x = w
        if y < 0: y = 0
        if y > h: y = h
        return (x, y)
    
    def getStats(self):
        stats = []
        for cannon in self.population:
            stats.append(cannon.getStats())

# Init 100 cannons at 0, 0
sim = Simulator(100, 0, 0)
sim.initBounds(100, 100)
sim.initTarget(40, 40, 10)

for epoch in range(0, 1):
    hit, out, _ = sim.fire()
    print(len(hit))
    sim.setPopulation(hit)
    sim.reproduce(10, 0, 0)
    print(len(sim.getPopulation()))
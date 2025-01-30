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
    def __init__(self, population):
        self.population = population.toList()

    # Init a target from the bottom left corner
    def initTarget(self, x1, y1, w):
        self.target = (x1, y1, x1 + w, y1 + w)

    def initBounds(self, w, h):
        self.dimensions = (w, h)

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
                    hitBounds.append(cannon)
                    self.population.remove(cannon)
            t += step
        print("Results:")
        print(len(hitTarget), "hit the target")
        print(len(hitBounds), 'hit the simulator bounds')
        return hitTarget, hitBounds, t
    
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

population = population.Population()
simulator = Simulator(population)
simulator.initBounds(75, 75)
simulator.initTarget(10, 0, 10)
hit, out, t = simulator.fire()
targetc = (simulator.target[0] + simulator.target[2]) / 2, (simulator.target[1] + simulator.target[3]) / 2
for cannon in out:
    tx, ty = targetc
    x, y = cannon.fire(t)
    dist = math.sqrt((ty-y)**2 + (tx-x)**2)
    print(dist)
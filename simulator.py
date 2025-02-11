# simulator.py
# Handles the environment where cannons "shoot"

import population
import cannon
import math
import random

class Simulator:
    target = (0, 0, 0, 0)
    dimensions = (100, 100)

    # Init a simulation environment with a population of cannons
    def __init__(self):
        pass

    # Init a square target from the bottom left corner
    def initTarget(self, x1, y1, w):
        self.target = (x1, y1, x1 + w, y1 + w)

    # Init dimensions of simulator
    def initBounds(self, w, h):
        self.dimensions = (w, h)

    def evolve(thresh, mA, mB):
        pass

    # Fire all cannons, recording the closest distance they came to the target
    def fire(self, population : population, step=0.1, max=3):
        hit = []
        minDist = [1000000 for i in range(0, self.getPopulation()).size()]

        # For each cannon in population
        for i in range(0, len(self.getPopulation())):
            cannon = self.getPopulation()[i]
            t = 0
            while t < max:
                result = cannon.fire(t)

                dist = self.distToTarget(result)
                if dist < minDist[i]:
                    minDist[i] = dist

                if self.inTarget(result):
                    hit.append(cannon)
                    break
                elif not self.inBounds(result):
                    break
                t += step

        return hit, minDist
    
    # Select all cannons from a population under a threshold t
    def select(self, thresh, cannons, dists):
        selected = []
        for i in range(0, len(cannons)):
            if dists[i] <= thresh:
                selected.append(cannons[i])
        return selected

    # Check if the projectile is in the target
    def inTarget(self, coord):
        x, y = coord
        x0, y0, x1, y1 = self.getTarget()
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
    
    # Get target coordinates
    def getTarget(self):
        return self.target
    
    # Get the coords of the center of the target
    def getTargetCenter(self):
        x0, y0, x1, y1 = self.getTarget()
        return (x1 + x0) / 2, (y1 + y0) / 2

    # Find the distance from a coordinate to the center of the target
    def distToTarget(self, coord):
        tx, ty = self.getTargetCenter()
        x, y = coord
        return 0 if self.inTarget(coord) else math.sqrt((ty-y)**2 + (tx-x)**2)
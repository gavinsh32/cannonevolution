# cannon.py
# Gavin Haynes
# Defines a Cannon object, which reperesents an entity that fires
# projectiles.

import random
import math

GENE_LEN = 90

# Cannon entity simulates a projectile launcher
class Cannon:
    tiltGene = None
    powerGene = None
    x = 0
    y = 0

    # Initialize a new Cannon entity with random genes and a position.
    def __init__(self, x, y):
        self.tiltGene = [('A' if random.randint(0, 1) == 1 else 'C') for i in range(0, GENE_LEN)]
        self.powerGene = [('A' if random.randint(0, 1) == 1 else 'C') for i in range(0, GENE_LEN)]
        self.x = x
        self.y = y

    # Count A's to calculate tilt and power.
    def calcStats(self):
        tilt = 0
        power = 0
        for i in range(0, GENE_LEN):
            tilt += 1 if self.tiltGene[i] == 'A' else 0
            power += 1 if self.powerGene[i] == 'A' else 0
        return (float(tilt), float(power))

    # Decompose tilt and power in to x and y velocities.
    def decompose(self):
        tilt, power = self.calcStats()
        tilt = tilt * math.pi / 180     # convert tilt to rads
        return (power*math.cos(tilt), power*math.sin(tilt))
    
    # Calculate the position of the cannon's projectile after t seconds.
    def fire(self, t):
        vx, vy = self.decompose()
        x0, y0 = self.x, self.y
        g = 9.81
        xf = x0 + vx*t
        yf = y0 + vy*t - (g * t ** 2) / 2
        return (xf, yf)

    def getVelocity(self):
        return self.decompose()

    def getStats(self):
        return self.calcStats()

    def getTiltGene(self):
        return self.tiltGene

    def getPowerGene(self):
        return self.powerGene
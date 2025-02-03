# simulator.py
# Handles the environment where cannons "shoot"

import population
import cannon
import math
import random

import pandas as pd
import matplotlib.pyplot as plt

# Fire cannons
# Should remove population as it just overcomplicates it
# while checking collision at each step:
#   if hit the target, add to success list
#   if fell out of bounds, check error distance
# select all success cannons and some that missed
# reproduce

class Simulator:
    population = []
    target = (0, 0, 0, 0)
    dimensions = (100, 100)

    # Init a simulation environment with a population of cannons
    def __init__(self, n=100, x=0, y=0):
        self.population = [cannon.Cannon(x, y) for i in range(0, n)]

    # Init a target from the bottom left corner
    def initTarget(self, x1, y1, w):
        self.target = (x1, y1, x1 + w, y1 + w)

    def initBounds(self, w, h):
        self.dimensions = (w, h)

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
        print("Results:")
        print(len(hitTarget), "hit the target")
        print(len(hitBounds), 'hit the simulator bounds')
        return hitTarget, hitBounds, t
    
    def reproduce(self, n):
        for i in range(0, len(self.population)):
            for j in range(0, random.randint(0, n)):
                self.population.append(self.population[i].copy())

    # Mutate n characters in both tilt and power gene for all cannons
    def mutateAll(self, n):
        for cannon in self.population:
            cannon.mutateTilt(n)
            cannon.mutatePower(n)

    def mutateTilt(self, n):
        for cannon in self.population:
            cannon.mutateTilt(n)

    def mutatePower(self, n):
        for cannon in self.population:
            cannon.mutatePower(n)

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

# Init 100 cannons at 0, 0
sim = Simulator(100, 0, 0)
sim.initBounds(100, 100)
sim.initTarget(40, 40, 10)
last = []

generations_fig = []
targets_hit_fig = []

for i in range(0, 10):
    print('\nGeneration', i)
    hit, out, t = sim.fire()
    last = hit
    sim.setPopulation(hit)
    sim.reproduce(6)
    sim.mutateAll(5)
    generations_fig.append(i)
    targets_hit_fig.append(len(hit))

data = {
    'targets_hit': targets_hit_fig,
    'time': generations_fig
}
df = pd.DataFrame(data)

df.plot(x='time', y='targets_hit', kind='line', 
        title='Targets Hit Over Time', 
        xlabel='Time (Generations)', 
        ylabel='Targets Hit', 
        grid=True, 
        figsize=(8, 5))

# Display the plot
plt.savefig("plot.png")
print("Plot saved to plot.png")


# # for distance in hit_dist:
# #     #point = df[df['distance'] == distance]
# #     #plt.scatter(point['time'], point['distance'], color='red', s=100, label=f'Hit: {time}')
# #     plt.axhline(y=distance, color='red', linestyle='--', label=f'Hit Distance: {distance}m')

# for distance in hit_dist:
#     point = df[df['distance'] == distance]
#     plt.scatter(point['generations', point['distance'], color='red', s=100, label=f'Hit: {distance}'])

# # Display the plot
# plt.savefig("plot.png")
# print("Plot saved to plot.png")

# for i in range(0, epocs):
#   1. generate population
#   2. fire cannons -> get those that hit target, those that went out of bounds
#   3. collect stats
#   4. replicate cannons that hit and form a new population
#   5. mutate
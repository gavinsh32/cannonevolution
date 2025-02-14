# main.py
# Gavin Haynes, Sam Beal
# Simulate and evolve virtual cannons.

import simulator
import population
import cannon
import random

import matplotlib.pyplot as plt
import pandas

width = 100
height = 100
targetx = 50
targety = 50
targetw = 10
psize = 50
gensize = 50

sim = simulator.Simulator()
sim.initBounds(width, height)
sim.initTarget(targetx, targety, width)

pop = population.Population(n=psize)

for epoch in range(0, gensize):
    dists = pop.fire()
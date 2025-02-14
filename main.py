# main.py
# Gavin Haynes, Sam Beal
# Simulate and evolve virtual cannons.

import simulator
import population
import cannon

width = 100
height = 100
targetx = 80
targety = 50
targetw = 10
psize = 25

sim = simulator.Simulator()
sim.initBounds(width, height)
sim.initTarget(targetx, targety, width)

pop = population.Population(n=psize)

for epoch in range(0, 30):

    print('Generation', epoch, 'population size', pop.size())

    # Fire cannons, get a list of how close they came
    dists = sim.fire(pop)

    # Select fit individuals based on the closest each came to the target
    fit = sim.select(pop, dists, 20)

    print('Success:', int(fit.size() / pop.size() * 100), 'percent')

    # Mutate children
    fit.mutateTilt(10, 3)
    fit.mutatePower(0, 0)

    fit.cull(70)

    # Cull initial population
    pop.cull(10)

    # Add children to population
    pop.join(fit)

    # Repeat for each generation
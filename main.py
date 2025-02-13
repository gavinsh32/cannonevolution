# main.py
# Gavin Haynes, Sam Beal
# Simulate and evolve virtual cannons.

import simulator
import population
import cannon

width = 100
height = 100
targetx = 50
targety = 50
targetw = 10
psize = 100

sim = simulator.Simulator()
sim.initBounds(width, height)
sim.initTarget(targetx, targety, width)

pop = population.Population(n=psize)

for epoch in range(0, 1):

    print('Generation', epoch, 'population size', pop.size())

    # Fire cannons, get a list of how close they came
    result = sim.fire(pop)

    # Select fit individuals based on the closest each came to the target
    fit = sim.select(pop, result, 10)

    print('Success:', fit.size() / pop.size())
    
    # Reproduce fit individuals
    children = fit.reproduce(10)

    print(children.getStats())

    # Mutate children
    #children.mutateTilt(5, 3)
    #children.mutatePower(5, 2)

    # Cull initial population
    #pop.cull(5)

    # Add children to population
    #pop.join(children)

    # Repeat for each generation
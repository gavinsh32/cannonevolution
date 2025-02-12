# main.py
# Gavin Haynes, Sam Beal
# Simulate and evolve virtual cannons.

import simulator
import population
import cannon

def main():
    bounds = 100, 100
    target = 60, 60, 10
    psize = 100

    sim = simulator.Simulator()
    sim.initBounds(bounds)
    sim.initTarget(target)

    pop = population.Population(n=psize)

    for epoch in range(0, 1):
        print('Generation', epoch, 'population size', pop.size())
        
        # Fire cannons, get a list of how close they came
        result = sim.fire(pop)

        fit = sim.select(pop, result, 10)
        print(fit.size())

if __name__ == '__main__':
    main()
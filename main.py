# main.py
# Gavin Haynes, Sam Beal
# Simulate and evolve virtual cannons.

import simulator
import population

def main():
    sim = simulator.Simulator()
    sim.initBounds(100, 100)
    sim.initTarget(60, 50, 10)

    pop = population.Population(n=20)

    for epoch in range(0, 10):
        print('Generation', epoch, 'population size', pop.size())
        winners = sim.fire(pop, 100)
        print(winners.size())

if __name__ == '__main__':
    main()
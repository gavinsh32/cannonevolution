# main.py
# Gavin Haynes, Sam Beal
# Simulate and evolve virtual cannons.

import simulator
import population

def main():
    sim = simulator.Simulator()
    sim.initBounds(100, 100)
    sim.initTarget(50, 50, 10)

    pop = population.Population(25)
    print(pop.size())
    pop2 = population.Population(5)
    pop.append(pop2)
    print(pop.size())

if __name__ == '__main__':
    main()
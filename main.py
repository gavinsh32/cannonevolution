# main.py
# Gavin Haynes, Sam Beal
# Simulate and evolve virtual cannons.

import simulator
import population

def main():
    pop = population.Population(25)
    print(pop.getStats())
    pop.mutateTilt(3)
    print(pop.getStats())

if __name__ == '__main__':
    main()
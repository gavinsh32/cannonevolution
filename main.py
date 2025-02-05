# main.py
# Gavin Haynes, Sam Beal
# Simulate and evolve virtual cannons.

import simulator

def main():
    sim = simulator.Simulator(100, 0, 0)    # Init 100 cannons at 0, 0
    sim.initBounds(200, 200)                # Set bounds to 200m by 200m
    sim.initTarget(40, 40, 20)              # Place a 20m by 20m target at 40, 40

    generations = []

    for epoch in range(0, 1):
        prev = sim.copy()           # Initial population
        generations.append(prev) 
        hit, min = sim.fire(0.2, 4)
        newpop = sim.select(10, hit, min)
        print(len(newpop))
        # succ = len(hit) / len(prev) * 100
        # print('Generation', epoch, 'success:', succ)
        # sim.setPopulation(hit)
        # sim.reproduce(2, 0, 0)
        #   print(len(sim.getPopulation()))

if __name__ == '__main__':
    main()
# main.py
# Gavin Haynes, Sam Beal
# Simulate and evolve virtual cannons.

import simulator
import population
import cannon
import pandas
import matplotlib.pyplot as plt

# Simulation settings
width = 100
height = 100
targetx = 80
targety = 50
targetw = 10
psize = 25
mrate = 9

sim = simulator.Simulator()
sim.initBounds(width, height)
sim.initTarget(targetx, targety, width)

runs = []

epochindex = [int(i) for i in range(0, 30)]
runindex = [i for i in range(0, 3)]

for run in runindex:

    generations = []
    pop = population.Population(n=psize)

    for epoch in epochindex:

        # Fire cannons, get a list of how close they came
        dists = sim.fire(pop)       
        # Select fit individuals based on the closest each came to the target
        fit = sim.select(pop, dists, 0)        

        # Record success
        generations.append(fit.size() / pop.size())

        # Mutate children
        fit.mutateTilt(mrate, 5)
        fit.mutatePower(0, 0)  

        fit.cull(70)       
        pop.cull(10)        

        # Add children to population
        pop.join(fit)      

        # Repeat for each generation

    runs.append(generations)

# Calculate average success at each generation in every run
gen_avgs = []
for gen in epochindex:
    avg = 0
    for run in runindex:
        avg += runs[run][gen]
    gen_avgs.append(avg / len(runindex))
    #print('Generation', gen, 'avg:', avg / len(runindex))

data = {'generation': epochindex, 'average_success': gen_avgs}
dframe = pandas.DataFrame(data)

dframe.plot(
    x='generation',
    y='average_success',
    title='Mutation Rate: ' + repr(mrate) + '% vs. Success',
    kind='line',
    xlabel='Generation',
    ylabel='% Hit Target',
    grid=True,
    figsize=(7,7)
)

plt.savefig(repr(mrate) + '.png')
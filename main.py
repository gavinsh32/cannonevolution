# main.py
# Gavin Haynes, Sam Beal
# Simulate and evolve virtual cannons.

import simulator
import population
import cannon
import random

import matplotlib.pyplot as plt
import pandas
#import numpy as np

width = 100
height = 100
targetx = 50
targety = 50
targetw = 10
#psize = 100
gensize = 30

#sim = simulator.Simulator()
# sim.initBounds(width, height)
# sim.initTarget(targetx, targety, width)

#pop = population.Population(n=psize)

def generation(psize, reproduction_rate):
    sim = simulator.Simulator()
    sim.initBounds(width, height)
    sim.initTarget(targetx, targety, width)
    pop = population.Population(n=psize)
    time = []
    success_rate = []
    
    for epoch in range(0, gensize):

        print('Generation', epoch, 'population size', pop.size())
        time.append(epoch)
        # Fire cannons, get a list of how close they came
        result = sim.fire(pop)

        # Select fit individuals based on the closest each came to the target
        fit = sim.select(pop, result, 10)

        success = fit.size() / pop.size()
        print('Success:', success)
        success_rate.append(success)
        
        # Reproduce fit individuals
        children = fit.reproduce(reproduction_rate)

        #print(children.getStats())

        # Mutate children
        children.mutateTilt(5, 3)
        children.mutatePower(5, 2)
        # a = random.randint(1, 10)
        # b = random.randint(1, 10)
        # c = random.randint(1, 10)
        # d = random.randint(1, 10)
        # children.mutateTilt(a,b)
        # children.mutatePower(c,d)

        # Cull initial population
        pop.cull(5)

        # Add children to population
        pop.join(children)

    return time, success_rate
        # Repeat for each generation
    
count = 0
############################## EXPERIMENTS
time, success_rate = generation(100, 10)
data = {'time': time, 'success_rate': success_rate }
dataframe = pandas.DataFrame(data)
dataframe.plot(x='time', y='success_rate', kind='line', 
       title='Population Size 100, Reproduce 10%, Cull 5%', 
       xlabel='Time (Generations)', 
       ylabel='Distance to target', 
       grid=True, 
       figsize=(8, 7))
plt.savefig("plot.png")
print("Plot saved to plot.png")
count +=1
##############################
time, success_rate = generation(1000, 10)
data = {'time': time, 'success_rate': success_rate }
dataframe = pandas.DataFrame(data)
dataframe.plot(x='time', y='success_rate', kind='line', 
       title='Population Size 1000, Reproduce 10%, Cull 5%', 
       xlabel='Time (Generations)', 
       ylabel='Distance to target', 
       grid=True, 
       figsize=(8, 7))
plt.savefig("plot2.png")
print("Plot saved to plot.png")
count +=1
##############################
time, success_rate = generation(500, 10)
data = {'time': time, 'success_rate': success_rate }
dataframe = pandas.DataFrame(data)
dataframe.plot(x='time', y='success_rate', kind='line', 
       title='Population Size 500, Reproduce 10%, Cull 5%', 
       xlabel='Time (Generations)', 
       ylabel='Distance to target', 
       grid=True, 
       figsize=(8, 7))
plt.savefig("plot3.png")
print("Plot saved to plot.png")
count +=1

# REPRODUCTION RATE
##############################
time, success_rate = generation(100, 20)
data = {'time': time, 'success_rate': success_rate }
dataframe = pandas.DataFrame(data)

dataframe.plot(x='time', y='success_rate', kind='line', 
       title='Population Size 100, Reproduce 20%, Cull 5%', 
       xlabel='Time (Generations)', 
       ylabel='Distance to target', 
       grid=True, 
       figsize=(8, 7))
plt.savefig("plot4.png")
print("Plot saved to plot.png")
count +=1
##############################
time, success_rate = generation(1000, 20)
data = {'time': time, 'success_rate': success_rate }
dataframe = pandas.DataFrame(data)
dataframe.plot(x='time', y='success_rate', kind='line', 
       title='Population Size 1000, Reproduce 20%, Cull 5%', 
       xlabel='Time (Generations)', 
       ylabel='Distance to target', 
       grid=True, 
       figsize=(8, 7))
plt.savefig("plot5.png")
print("Plot saved to plot.png")
count +=1


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
    
    
    
    
    # we cover 
        # Fitness
        # Selection 
        # Reproduction
        # Evolution 
    
    # Experiments:
        # Reproduction Rate
        # Cull rate
        # Mutation rate
        # Population size
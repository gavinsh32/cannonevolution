from population import Population

saved_data = []

class Data:
    def __init__(self):
        self.powera = 0
        self.powerc = 0
        self.tilta = 0
        self.tiltc = 0
        self.power_index = 0
        self.tilt_index = 0
    def power_count(self, power_a, power_c, i):
      self.powera = power_a
      self.powerc = power_c
      self.power_index = i

    def tilt_count(self, tilt_a, tilt_c, i):
      self.tilta = tilt_a
      self.tiltc = tilt_c
      self.tilt_index = i

def analyze_sequence(children):
    power = children.getPowerGenes()
    tilt = children.getTiltGenes()

    num = []
    index = 0
   
    for i in range(len(power)):  # Fixed unpacking

        curr_data = Data()
        a = 0
        c = 0
        for j, amino in enumerate(power):  # Fixed inner loop
            if amino[j] == 'A': 
                a += 1
            else: 
                c += 1
        curr_data.power_count(a,c,i)
        #print(f"A_count: {a} C_count: {c}")
        a = 0
        c = 0
        for j, amino in enumerate(tilt):  # Fixed inner loop
            if amino[j] == 'A': 
                a += 1
            else: 
                c += 1
        curr_data.tilt_count(a,c,i)
        num.append(curr_data)
        #print(f"A_count: {a} C_count: {c}")

    similar_power = 100
    similar_tilt = 100
    similar_power_genome = num[0]
    similar_tilt_genome = num[0]
    for i in range(len(num)):
        for j in range(len(num)):  # Added missing colon
            # Continue your logic here
            curr_power = abs(num[i].powera - num[j].powera) + abs(num[i].powerc - num[j].powerc) 
            curr_tilt = abs(num[i].tilta - num[j].tilta) + abs(num[i].tilta - num[j].tiltc) 
            if (similar_power > curr_power): 
               similar_power = curr_power
               similar_power_genome = num[j]
            if (similar_tilt > curr_tilt): 
               similar_tilt = curr_tilt
               similar_tilt_genome = num[j]

              # Placeholder to avoid syntax error

   #  print(power[similar_genome.index])
   #  print(tilt[similar_genome.index])
    print(f"A count: {similar_tilt_genome.tilta}")
    print(f"C count: {similar_tilt_genome.tiltc}")
    print(f"A count: {similar_power_genome.powera}")
    print(f"C count: {similar_power_genome.powerc}")
    print(f"Similar score: {similar_tilt}")
    print(f"Similar score: {similar_power}")
    saved_data.append(num)

import pandas as pd
import matplotlib.pyplot as plt

def graphs_generations(generations):
    global saved_data

    if not saved_data:  # Ensure there is data to process
        print("No data available to plot.")
        return

    if not isinstance(generations, list) or not all(isinstance(x, int) for x in generations):
        print("Error: generations must be a list of integers.")
        return

    # Extracting data from instances of Data class
    power_a = [d.powera for sublist in saved_data for d in sublist]
    power_c = [d.powerc for sublist in saved_data for d in sublist]
    tilt_a = [d.tilta for sublist in saved_data for d in sublist]
    tilt_c = [d.tiltc for sublist in saved_data for d in sublist]

    # TRIM if needed
    # Ensure we have enough data points to match the generations list
    min_length = min(len(generations), len(power_a))
    generations = generations[:min_length]
    power_a = power_a[:min_length]
    power_c = power_c[:min_length]
    tilt_a = tilt_a[:min_length]
    tilt_c = tilt_c[:min_length]

    # Creating DataFrame
    data = {'time': generations, 'power_a': power_a, 'power_c': power_c, 'tilt_a': tilt_a, 'tilt_c': tilt_c}
    dataframe = pd.DataFrame(data)

    # Plotting the data
    dataframe.plot(x='time', y=['power_a', 'power_c', 'tilt_a', 'tilt_c'], kind='line', 
                   title='Gene Count Over Time', 
                   xlabel='Time (Generations)', 
                   ylabel='Count', 
                   grid=True, 
                   figsize=(8, 7))

    # Saving the plot
    plt.savefig("analyze_generations.png")
    plt.show()  # To display the graph in interactive environments
    print("Plot saved to analyze.png")


def graphs_children():
    global saved_data

    if not saved_data:  # Ensure there is data to process
        print("No data available to plot.")
        return

    # Extracting data from instances of Data class
    power_a = [d.powera for sublist in saved_data for d in sublist]
    power_c = [d.powerc for sublist in saved_data for d in sublist]
    tilt_a = [d.tilta for sublist in saved_data for d in sublist]
    tilt_c = [d.tiltc for sublist in saved_data for d in sublist]
    time = list(range(len(power_a)))  # Use the length of extracted data

    # Creating DataFrame
    data = {'time': time, 'power_a': power_a, 'power_c': power_c, 'tilt_a': tilt_a, 'tilt_c': tilt_c}
    dataframe = pd.DataFrame(data)

    # Plotting the data
    dataframe.plot(x='time', y=['power_a', 'power_c', 'tilt_a', 'tilt_c'], kind='line', 
                   title='Gene Count Over Time', 
                   xlabel='Time (Children Over Time)', 
                   ylabel='Count', 
                   grid=True, 
                   figsize=(8, 7))

    # Saving the plot
    plt.savefig("analyze_children.png")
    plt.show()  # To display the graph in interactive environments
    print("Plot saved to analyze.png")

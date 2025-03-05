from population import Population

# saved_data = []

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


# data = {'time': time, 'success_rate': success_rate }
# dataframe = pandas.DataFrame(data)
# dataframe.plot(x='time', y='success_rate', kind='line', 
#        title='Population Size 100, Reproduce 10%, Cull 5%', 
#        xlabel='Time (Generations)', 
#        ylabel='% Hit Target', 
#        grid=True, 
#        figsize=(8, 7))
# plt.savefig("analyze.png")
# print("Plot saved to analyze.png")

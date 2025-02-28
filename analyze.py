from population import Population

class Data:
    def __init__(self, aa, cc, i):
        self.a = aa
        self.c = cc
        self.index = i

def analyze_sequence(children):
    power = children.getPowerGenes()
    tilt = children.getTiltGenes()

    num = []
    index = 0

    for i, obj in enumerate(power):  # Fixed unpacking
        a = 0
        c = 0
        for j, amino in enumerate(obj):  # Fixed inner loop
            if amino == 'A': 
                a += 1
            else: 
                c += 1
        num.append(Data(a, c, i))  # Fixed list assignment
        #print(f"A_count: {a} C_count: {c}")

    similar = 100
    similar_genome = num[0]
    for i in range(len(num)):
        for j in range(len(num)):  # Added missing colon
            # Continue your logic here
            curr = abs(num[i].a - num[j].a) + abs(num[i].c - num[j].c) 
            if (similar > curr): 
               similar = curr
               similar_genome = num[j]
              # Placeholder to avoid syntax error

    print(power[similar_genome.index])
    print(tilt[similar_genome.index])

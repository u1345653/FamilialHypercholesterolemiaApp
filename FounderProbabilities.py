import numpy as np
from itertools import product

x = [i for i in product(range(2), repeat=9)]
x = np.array(x)
print(x)

dna_dx = int(input("Does patient have DNA DX? "))

def FPP1(x):
    fh_prob = 0.002
    right_side = 1
    trust = 0
    output = [trust] #list that the function will return
    for item in x:
        if item[0] > 0:
            trust = fh_prob * right_side
            output.append(trust) #append to the list instead of printing
        if item[0] == 0:
            trust = (1 - fh_prob) * right_side
            output.append(trust)
        if item[0] == 0 and dna_dx == 1:
            right_side = 0
            trust = (1 - fh_prob) * right_side
            output.append(trust)

    return output #return list of values


def FPP2(x):
    fh_prob = 0.002
    right_side = 1
    trust = 0
    output = [trust] #list that the function will return
    for item in x:
        if item[1] > 0:
            trust = fh_prob * right_side
            output.append(trust) #append to the list instead of printing
        if item[1] == 0:
            trust = (1 - fh_prob) * right_side
            output.append(trust)
        if item[1] == 0 and dna_dx == 1:
            right_side = 0
            trust = (1 - fh_prob) * right_side
            output.append(trust)
    return output #return list of values

def FPP3(x):
    fh_prob = 0.002
    right_side = 1
    trust = 0
    output = [trust] #list that the function will return
    for item in x:
        if item[2] > 0:
            trust = fh_prob * right_side
            output.append(trust) #append to the list instead of printing
        if item[2] == 0:
            trust = (1 - fh_prob) * right_side
            output.append(trust)
        if item[2] == 0 and dna_dx == 1:
            right_side = 0
            trust = (1 - fh_prob) * right_side
            output.append(trust)
    return output #return list of values


founderprob = np.array([FPP1(x), FPP2(x), FPP3(x)]).transpose()
founderdelete = np.delete(founderprob, (0), axis=0)
print(founderprob)



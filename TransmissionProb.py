from FounderProbabilities import x
from FounderProbabilities import dna_dx
import numpy as np


trans = x
transdna = dna_dx


def TP4(x):
    multiply = 1
    left_side = 0
    transprob = [left_side]
    for item in trans:
        if item[0] > 0 and item[1] > 0 and item[3] > 0:
            left_side = 0.75 * multiply
            transprob.append(left_side)
        if item[0] > 0 and item[1] > 0 and item[3] == 0:
            left_side = 0.25 * multiply
            transprob.append(left_side)
        if item[0] > 0 and item[1] == 0 and item[3] > 0:
            left_side = 0.5 * multiply
            transprob.append(left_side)
        if item[0] > 0 and item[1] == 0 and item[3] == 0:
            left_side = 0.5 * multiply
            transprob.append(left_side)
        if item[0] == 0 and item[1] > 0 and item[3] > 0:
            left_side = 0.5 * multiply
            transprob.append(left_side)
        if item[0] == 0 and item[1] > 0 and item[3] == 0:
            left_side = 0.5 * multiply
            transprob.append(left_side)
        if item[0] == 0 and item[1] == 0 and item[3] > 0:
            left_side = 0 * multiply
            transprob.append(left_side)
        if item[0] == 0 and item[1] == 0 and item[3] == 0:
            left_side = 1 * multiply
            transprob.append(left_side)
        if item[3] == 0 and transdna == 1:
            left_side = 0
            transprob.append(left_side)
    return transprob

def TP5(x):
    multiply = 1
    left_side = 0
    transprob = [left_side]
    for item in trans:
        if item[0] > 0 and item[1] > 0 and item[4] > 0:
            left_side = 0.75 * multiply
            transprob.append(left_side)
        if item[0] > 0 and item[1] > 0 and item[4] == 0:
            left_side = 0.25 * multiply
            transprob.append(left_side)
        if item[0] > 0 and item[1] == 0 and item[4] > 0:
            left_side = 0.5 * multiply
            transprob.append(left_side)
        if item[0] > 0 and item[1] == 0 and item[4] == 0:
            left_side = 0.5 * multiply
            transprob.append(left_side)
        if item[0] == 0 and item[1] > 0 and item[4] > 0:
            left_side = 0.5 * multiply
            transprob.append(left_side)
        if item[0] == 0 and item[1] > 0 and item[4] == 0:
            left_side = 0.5 * multiply
            transprob.append(left_side)
        if item[0] == 0 and item[1] == 0 and item[4] > 0:
            left_side = 0 * multiply
            transprob.append(left_side)
        if item[0] == 0 and item[1] == 0 and item[4] == 0:
            left_side = 1 * multiply
            transprob.append(left_side)
        if item[4] == 0 and transdna == 1:
            left_side = 0
            transprob.append(left_side)
    return transprob

def TP6(x):
    multiply = 1
    left_side = 0
    transprob = [left_side]
    for item in trans:
        if item[0] > 0 and item[1] > 0 and item[5] > 0:
            left_side = 0.75 * multiply
            transprob.append(left_side)
        if item[0] > 0 and item[1] > 0 and item[5] == 0:
            left_side = 0.25 * multiply
            transprob.append(left_side)
        if item[0] > 0 and item[1] == 0 and item[5] > 0:
            left_side = 0.5 * multiply
            transprob.append(left_side)
        if item[0] > 0 and item[1] == 0 and item[5] == 0:
            left_side = 0.5 * multiply
            transprob.append(left_side)
        if item[0] == 0 and item[1] > 0 and item[5] > 0:
            left_side = 0.5 * multiply
            transprob.append(left_side)
        if item[0] == 0 and item[1] > 0 and item[5] == 0:
            left_side = 0.5 * multiply
            transprob.append(left_side)
        if item[0] == 0 and item[1] == 0 and item[5] > 0:
            left_side = 0 * multiply
            transprob.append(left_side)
        if item[0] == 0 and item[1] == 0 and item[5] == 0:
            left_side = 1 * multiply
            transprob.append(left_side)
        if item[5] == 0 and transdna == 1:
            left_side = 0
            transprob.append(left_side)
    return transprob

def TP7(x):
    multiply = 1
    left_side = 0
    transprob = [left_side]
    for item in trans:
        if item[2] > 0 and item[5] > 0 and item[6] > 0:
            left_side = 0.75 * multiply
            transprob.append(left_side)
        if item[2] > 0 and item[5] > 0 and item[6] == 0:
            left_side = 0.25 * multiply
            transprob.append(left_side)
        if item[2] > 0 and item[5] == 0 and item[6] > 0:
            left_side = 0.5 * multiply
            transprob.append(left_side)
        if item[2] > 0 and item[5] == 0 and item[6] == 0:
            left_side = 0.5 * multiply
            transprob.append(left_side)
        if item[2] == 0 and item[5] > 0 and item[6] > 0:
            left_side = 0.5 * multiply
            transprob.append(left_side)
        if item[2] == 0 and item[5] > 0 and item[6] == 0:
            left_side = 0.5 * multiply
            transprob.append(left_side)
        if item[2] == 0 and item[5] == 0 and item[6] > 0:
            left_side = 0 * multiply
            transprob.append(left_side)
        if item[2] == 0 and item[5] == 0 and item[6] == 0:
            left_side = 1 * multiply
            transprob.append(left_side)
        if item[6] == 0 and transdna == 1:
            left_side = 0
            transprob.append(left_side)
    return transprob

def TP8(x):
    multiply = 1
    left_side = 0
    transprob = [left_side]
    for item in trans:
        if item[2] > 0 and item[5] > 0 and item[7] > 0:
            left_side = 0.75 * multiply
            transprob.append(left_side)
        if item[2] > 0 and item[5] > 0 and item[7] == 0:
            left_side = 0.25 * multiply
            transprob.append(left_side)
        if item[2] > 0 and item[5] == 0 and item[7] > 0:
            left_side = 0.5 * multiply
            transprob.append(left_side)
        if item[2] > 0 and item[5] == 0 and item[7] == 0:
            left_side = 0.5 * multiply
            transprob.append(left_side)
        if item[2] == 0 and item[5] > 0 and item[7] > 0:
            left_side = 0.5 * multiply
            transprob.append(left_side)
        if item[2] == 0 and item[5] > 0 and item[7] == 0:
            left_side = 0.5 * multiply
            transprob.append(left_side)
        if item[2] == 0 and item[5] == 0 and item[7] > 0:
            left_side = 0 * multiply
            transprob.append(left_side)
        if item[2] == 0 and item[5] == 0 and item[7] == 0:
            left_side = 1 * multiply
            transprob.append(left_side)
        if item[7] == 0 and transdna == 1:
            left_side = 0
            transprob.append(left_side)
    return transprob

def TP9(x):
    multiply = 1
    left_side = 0
    transprob = [left_side]
    for item in trans:
        if item[2] > 0 and item[5] > 0 and item[8] > 0:
            left_side = 0.75 * multiply
            transprob.append(left_side)
        if item[2] > 0 and item[5] > 0 and item[8] == 0:
            left_side = 0.25 * multiply
            transprob.append(left_side)
        if item[2] > 0 and item[5] == 0 and item[8] > 0:
            left_side = 0.5 * multiply
            transprob.append(left_side)
        if item[2] > 0 and item[5] == 0 and item[8] == 0:
            left_side = 0.5 * multiply
            transprob.append(left_side)
        if item[2] == 0 and item[5] > 0 and item[8] > 0:
            left_side = 0.5 * multiply
            transprob.append(left_side)
        if item[2] == 0 and item[5] > 0 and item[8] == 0:
            left_side = 0.5 * multiply
            transprob.append(left_side)
        if item[2] == 0 and item[5] == 0 and item[8] > 0:
            left_side = 0 * multiply
            transprob.append(left_side)
        if item[2] == 0 and item[5] == 0 and item[8] == 0:
            left_side = 1 * multiply
            transprob.append(left_side)
        if item[8] == 0 and transdna == 1:
            left_side = 0
            transprob.append(left_side)
    return transprob


transmissionprob = np.array([TP4(x), TP5(x), TP6(x), TP7(x), TP8(x), TP9(x)]).transpose()
print(transmissionprob)

import Penetrance
from FounderProbabilities import x
import numpy as np


penprob = x
notfh = Penetrance.ldlcnotfh(Penetrance.ldlc, Penetrance.age)
isfh = Penetrance.ldlcfh(Penetrance.ldlc, Penetrance.age)


def LDLC1():
    ldlcprob = 0
    ldlcoutput = [ldlcprob]
    for item in penprob:
        if item[0] == 0:
            ldlcprob = notfh
            ldlcoutput.append(ldlcprob)
        if item[0] == 1:
            ldlcprob = isfh
            ldlcoutput.append(ldlcprob)

    return ldlcoutput

def LDLC2():
    ldlcprob = 0
    ldlcoutput = [ldlcprob]
    for item in penprob:
        if item[1] == 0:
            ldlcprob = notfh
            ldlcoutput.append(ldlcprob)
        if item[1] == 1:
            ldlcprob = isfh
            ldlcoutput.append(ldlcprob)

    return ldlcoutput

def LDLC3():
    ldlcprob = 0
    ldlcoutput = [ldlcprob]
    for item in penprob:
        if item[2] == 0:
            ldlcprob = notfh
            ldlcoutput.append(ldlcprob)
        if item[2] == 1:
            ldlcprob = isfh
            ldlcoutput.append(ldlcprob)

    return ldlcoutput

def LDLC4():
    ldlcprob = 0
    ldlcoutput = [ldlcprob]
    for item in penprob:
        if item[3] == 0:
            ldlcprob = notfh
            ldlcoutput.append(ldlcprob)
        if item[3] == 1:
            ldlcprob = isfh
            ldlcoutput.append(ldlcprob)

    return ldlcoutput

def LDLC5():
    ldlcprob = 0
    ldlcoutput = [ldlcprob]
    for item in penprob:
        if item[4] == 0:
            ldlcprob = notfh
            ldlcoutput.append(ldlcprob)
        if item[4] == 1:
            ldlcprob = isfh
            ldlcoutput.append(ldlcprob)

    return ldlcoutput

def LDLC6():
    ldlcprob = 0
    ldlcoutput = [ldlcprob]
    for item in penprob:
        if item[5] == 0:
            ldlcprob = notfh
            ldlcoutput.append(ldlcprob)
        if item[5] == 1:
            ldlcprob = isfh
            ldlcoutput.append(ldlcprob)

    return ldlcoutput

def LDLC7():
    ldlcprob = 0
    ldlcoutput = [ldlcprob]
    for item in penprob:
        if item[6] == 0:
            ldlcprob = notfh
            ldlcoutput.append(ldlcprob)
        if item[6] == 1:
            ldlcprob = isfh
            ldlcoutput.append(ldlcprob)

    return ldlcoutput

def LDLC8():
    ldlcprob = 0
    ldlcoutput = [ldlcprob]
    for item in penprob:
        if item[7] == 0:
            ldlcprob = notfh
            ldlcoutput.append(ldlcprob)
        if item[7] == 1:
            ldlcprob = isfh
            ldlcoutput.append(ldlcprob)

    return ldlcoutput

def LDLC9():
    ldlcprob = 0
    ldlcoutput = [ldlcprob]
    for item in penprob:
        if item[8] == 0:
            ldlcprob = notfh
            ldlcoutput.append(ldlcprob)
        if item[8] == 1:
            ldlcprob = isfh
            ldlcoutput.append(ldlcprob)

    return ldlcoutput

ldlarray = np.array([LDLC1(), LDLC2(), LDLC3(), LDLC4(), LDLC5(), LDLC6(), LDLC7(), LDLC8(), LDLC9()]).transpose()
print(ldlarray)


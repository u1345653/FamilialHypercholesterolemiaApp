from scipy import stats
import math
import pandas as pd

def ldlcfh(age, ldlc, totalc):
    value1 = 0
    returnvar = 0
    meantrue = 0
    sdtrue = 0
    meanfalse = 0
    sdfalse = 0
    ldlcfhlessthan20mean = 205
    ldlcfh2030mean = 222
    ldlcfh30plusmean = 222
    ldlcfhlessthan20sd = 55
    ldlcfh2030sd = 76
    ldlcfh30plussd = 76
    ldlcnotfhlessthan20mean = 89
    ldlcnotfhlessthan20sd = 26
    ldlcnotfh2030mean = 105
    ldlcnotfh2030sd = 32
    ldlcnotfh30plusmean = 121
    ldlcnotfh30plussd = 35
    totalcfhlessthan20mean = 279
    totalcfhlessthan20sd = 58
    totalcfh2030mean = 309
    totalcfh2030sd = 61
    totalcfh30plusmean = 316
    totalcfh30plussd = 84
    totalcnotfhlessthan20mean = 158
    totalcnotfhlessthan20sd = 29
    totalcnotfh2030mean = 177
    totalcnotfh2030sd = 36
    totalcnotfh30plusmean = 201
    totalcnotfh30plussd = 41
    if ldlc > 0:
        if age < 20:
            value1 = 1
            meantrue = value1 * ldlcfhlessthan20mean
            sdtrue = value1 * ldlcfhlessthan20sd
            returnvar = stats.norm.pdf(ldlc, meantrue, sdtrue)
            # print(returnvar)
        elif 20 <= age < 30:
            value1 = 1
            meantrue = value1 * ldlcfh2030mean
            sdtrue = value1 * ldlcfh2030sd
            returnvar = stats.norm.pdf(ldlc, meantrue, sdtrue)
            # print(returnvar)
        elif age >= 30:
            value1 = 1
            meantrue = value1 * ldlcfh30plusmean
            sdtrue = value1 * ldlcfh30plussd
            returnvar = stats.norm.pdf(ldlc, meantrue, sdtrue)
            # print(returnvar)
        else:
            returnvar = 1
    else:
        if age < 20:
            value1 = 1
            meanfalse = value1 * totalcfhlessthan20mean
            sdfalse = value1 * totalcfhlessthan20sd
            returnvar = stats.norm.pdf(totalc, meanfalse, sdfalse)
            # print(returnvar)
        elif 20 <= age < 30:
            value1 = 1
            meanfalse = value1 * totalcfh2030mean
            sdfalse = value1 * totalcfh2030sd
            returnvar = stats.norm.pdf(totalc, meanfalse, sdfalse)
            # print(returnvar)
        elif age >= 30:
            value1 = 1
            meanfalse = value1 * totalcfh30plusmean
            sdfalse = value1 * totalcfh30plussd
            returnvar = stats.norm.pdf(totalc, meanfalse, sdfalse)
            # print(returnvar)
        else:
            returnvar = 1
    return returnvar

def ldlcnotfh(ldlc, age, totalc):
    value1 = 0
    returnvar = 0
    meantrue = 0
    sdtrue = 0
    meanfalse = 0
    sdfalse = 0
    ldlcfhlessthan20mean = 205
    ldlcfh2030mean = 222
    ldlcfh30plusmean = 222
    ldlcfhlessthan20sd = 55
    ldlcfh2030sd = 76
    ldlcfh30plussd = 76
    ldlcnotfhlessthan20mean = 89
    ldlcnotfhlessthan20sd = 26
    ldlcnotfh2030mean = 105
    ldlcnotfh2030sd = 32
    ldlcnotfh30plusmean = 121
    ldlcnotfh30plussd = 35
    totalcfhlessthan20mean = 279
    totalcfhlessthan20sd = 58
    totalcfh2030mean = 309
    totalcfh2030sd = 61
    totalcfh30plusmean = 316
    totalcfh30plussd = 84
    totalcnotfhlessthan20mean = 158
    totalcnotfhlessthan20sd = 29
    totalcnotfh2030mean = 177
    totalcnotfh2030sd = 36
    totalcnotfh30plusmean = 201
    totalcnotfh30plussd = 41
    if ldlc > 0:
        if age < 20:
            value1 = 1
            meantrue = value1 * ldlcnotfhlessthan20mean
            sdtrue = value1 * ldlcnotfhlessthan20sd
            returnvar = stats.norm.pdf(ldlc, meantrue, sdtrue)
            # print(returnvar)
        elif 20 <= age < 30:
            value1 = 1
            meantrue = value1 * ldlcnotfh2030mean
            sdtrue = value1 * ldlcnotfh2030sd
            returnvar = stats.norm.pdf(ldlc, meantrue, sdtrue)
            # print(returnvar)
        elif age >= 30:
            value1 = 1
            meantrue = value1 * ldlcnotfh30plusmean
            sdtrue = value1 * ldlcnotfh30plussd
            returnvar = stats.norm.pdf(ldlc, meantrue, sdtrue)
            # print(returnvar)
        else:
            returnvar = 1
    else:
        if age < 20:
            value1 = 1
            meanfalse = value1 * totalcnotfhlessthan20mean
            sdfalse = value1 * totalcnotfhlessthan20sd
            returnvar = stats.norm.pdf(totalc, meanfalse, sdfalse)
            # print(returnvar)
        elif 20 <= age < 30:
            value1 = 1
            meanfalse = value1 * totalcnotfh2030mean
            sdfalse = value1 * totalcnotfh2030sd
            returnvar = stats.norm.pdf(totalc, meanfalse, sdfalse)
            # print(returnvar)
        elif age >= 30:
            value1 = 1
            meanfalse = value1 * totalcnotfh30plusmean
            sdfalse = value1 * totalcnotfh30plussd
            returnvar = stats.norm.pdf(totalc, meanfalse, sdfalse)
            # print(returnvar)
        else:
            returnvar = 1
    return returnvar

def TXPFISFH(ldlc, age, tx):
    calc = 0
    if tx == 9:
        calc = 1
        # print(calc)
    else:
        if ldlc > 100:
            calc = tx * ((0.8205 * age-1.8113)/100) + (1-tx) * (1-(0.8205 * age - 1.8113)/100)
            # print(calc)
        else:
            calc = tx * 1 + (1-tx) * 1
            # print(calc)
    return calc


def TXPFISNOTFH(tx):
    calc = 0
    if tx == 9:
        calc = 1
        # print(calc)
    else:
        if tx == 1:
            calc = 0.0001
            # print(calc)
        else:
            calc = 1 - 0.0001
            # print(calc)
    return calc

def CADPFISFH(clinicalCAD, gender, onsetAge, age):
    calc = 0
    if clinicalCAD == 9:
        calc = 1
        # print(calc, "Line 188")
    else:
        if gender == "m":
            if clinicalCAD == 1:
                calc = 0.832/(1+math.exp(0.124*(52.9-onsetAge)))
                # print(calc, "Line 193")
            else:
                calc = 1 - (0.832/(1+math.exp(0.124*(52.9-age))))
                # print(calc, "Line 196")
        else:
            if clinicalCAD == 1:
                calc = 0.601/(1+math.exp(0.155*(54.7-onsetAge)))
                # print(calc, "Line 200")
            else:
                calc = 1-(0.601/(1+math.exp(0.155*(54.7-age))))
                # print(calc, "Line 203")
    return calc


def CADISNOTFH(clinicalCAD, gender, onsetAge, age):
    calc = 0
    if clinicalCAD == 9:
        calc = 1
        # print(calc, " Line 210")
    else:
        if gender == "m":
            if clinicalCAD == 1:
                calc = 0.499/(1 + math.exp(0.142*(69.6-onsetAge)))
                # print(calc, " Line 215")
            else:
                calc = 1-(0.499/(1+math.exp(0.142*(69.6-age))))
                # print(calc, " Line 218")
        else:
            if clinicalCAD == 1:
                calc = 0.713/(1+math.exp(0.0981*(88.6-onsetAge)))
                # print(calc, "Line 222")
            else:
                calc = 1-(0.713/(1+math.exp(0.0981*(88.6-age))))
                # print(calc, "Line 225")
    return calc

familynumber = int(input("How many family member info do you have? Please select from 1 - 9: "))

# Define the dataframe
pinput = pd.DataFrame(columns=["age", "ldlc", "totalc", "gender", "clinicalCAD", "onsetAge", "tx", "dna_dx"])

# Use range to go in a loop
for i in range(familynumber):
    age = int(input("Please enter your Age: "))
    ldlc = int(input("Please enter you LDL-C Level: "))
    totalc = int(input("Please enter your Total-C Level: "))
    gender = input("Please enter a gender ").lower()
    clinicalCAD = int(input("Does someone have clinical CAD: "))
    onsetAge = int(input("Please enter CAD onset age: "))
    tx = int(input("Does someone have Tandon Xanthoma: "))
    dna_dx = int(input("Does patient have DNA DX? "))

    # Add row by row to the dataframe
    pinput.loc[i] = [age, ldlc, totalc, gender, clinicalCAD, onsetAge, tx, dna_dx]

# print head to verify
# print(pinput)



def multiple():
    output = pd.DataFrame(columns=['ldlcfh1', 'ldlcnotfh1', 'txpfisfh1', 'txpfisnotfh1', 'cadpfisfh1', 'cadisnotfh1'])
    for i, j in pinput.iterrows():
        agei =j.values[0]
        ldlci = j.values[1]
        totalci = j.values[2]
        clincalcad = j.values[4]
        genderi = j.values[3]
        onsetage = j.values[5]
        txi = j.values[6]
        # print("First Person " + str(i) + "-" + str(j))
        # print("ldlcfh called with " + str(agei) + " " + str(ldlci))
        ldlcfh1 = ldlcfh(agei, ldlci, totalci)
        # print("ldlcfh1 is equal to " + str(ldlcfh1))
        # print("txpfisfh called with " + str(ldlci) + " " + str(agei) + " " + str(txi))
        txpfisfh1 = TXPFISFH(ldlci, agei, txi)
        # print("txpfish1 is equal to " + str(txpfisfh1))
        # print("cadpfish called with " + str(clincalcad) + " " + str(genderi) + " " + str(onsetage) + " " + str(agei))
        cadpfish1 = CADPFISFH(clincalcad, genderi, onsetage, agei)
        # print("cadpfisfh1 is equal to " + str(cadpfish1))
        # print("ldlcnotfh called with " + str(ldlci) + " " + str(agei))
        ldlcnotfh1 = ldlcnotfh(ldlci, agei, totalci)
        # print("ldlcnotfh1 is equal to " + str(ldlcnotfh1))
        # print("txpfisnotfh called with " + str(txi))
        txpfisnotfh1 = TXPFISNOTFH(txi)
        # print("txpfish1 is equal to " + str(txpfisnotfh1))
        # print("cadisnotfh called with " + " " + str(clincalcad) + " " + str(genderi) + " " + str(onsetage) + " " + str(agei))
        cadisnotfh1 = CADISNOTFH(clincalcad, genderi, onsetage, agei)
        # print("cadisfnoth1 is equal to " + str(cadisnotfh1))
        output.loc[i] = [ldlcfh1, ldlcnotfh1, txpfisfh1, txpfisnotfh1, cadpfish1, cadisnotfh1]
    # print(output)
    return output

multiple()

import numpy as np
from itertools import product
import pandas as pd
import sys
binary = [i for i in product(range(2), repeat=9)]
binary = np.array(binary)
# print(x)

# print(dna_dx1)

# print(dna_dx2)

# print(dna_dx3)

def FPP1():
    dna_dx1 = pinput.iloc[[0], [7]]
    fh_prob = 0.002
    trust = 0
    output = [trust] #list that the function will return
    for item in binary:
        if dna_dx1.values == 1 and item[0] == 0:
            right_side = 0
            trust = (1 - fh_prob) * right_side
            output.append(trust)
            # print("Line 303 ", trust)
        else:
            if item[0] > 0:
                right_side = 1
                trust = fh_prob * right_side
                output.append(trust) #append to the list instead of printing
                # print("Line 308 ", trust)
            else:
                right_side = 1
                trust = (1 - fh_prob) * right_side
                output.append(trust)
                # print("Line 312 ", trust)
    return output #return list of values

def FPP2():
    dna_dx2 = pinput.iloc[[1], [7]]
    fh_prob = 0.002
    trust = 0
    output = [trust] #list that the function will return
    for item in binary:
        if dna_dx2.values == 1 and item[1] == 0:
            right_side = 0
            trust = (1 - fh_prob) * right_side
            output.append(trust)
            # print("Line 303 ", trust)
        else:
            if item[1] > 0:
                right_side = 1
                trust = fh_prob * right_side
                output.append(trust) #append to the list instead of printing
                # print("Line 308 ", trust)
            else:
                right_side = 1
                trust = (1 - fh_prob) * right_side
                output.append(trust)
                # print("Line 312 ", trust)
    return output #return list of values

def FPP3():
    dna_dx3 = pinput.iloc[[2], [7]]
    fh_prob = 0.002
    trust = 0
    output = [trust] #list that the function will return
    for item in binary:
        if dna_dx3.values == 1 and item[2] == 0:
            right_side = 0
            trust = (1 - fh_prob) * right_side
            output.append(trust)
            # print("Line 303 ", trust)
        else:
            if item[2] > 0:
                right_side = 1
                trust = fh_prob * right_side
                output.append(trust) #append to the list instead of printing
                # print("Line 308 ", trust)
            else:
                right_side = 1
                trust = (1 - fh_prob) * right_side
                output.append(trust)
                # print("Line 312 ", trust)
    return output #return list of values


pd.set_option('display.max_rows', None)
founder = pd.DataFrame([FPP1(), FPP2(), FPP3()]).transpose()
founderprob = founder.iloc[1:,:]
# print(founderprob)

def TP4():
    transdna4 = pinput.iloc[[3], [7]]
    left_side = 0
    transprob4 = [left_side]
    for item in binary:
        if item[3] == 0 and transdna4.values == 1:
            left_side = 0
            transprob4.append(left_side)
        else:
            if item[0] > 0 and item[1] > 0 and item[3] > 0:
                multiply = 1
                left_side = 0.75 * multiply
                transprob4.append(left_side)
            elif item[0] > 0 and item[1] > 0 and item[3] == 0:
                multiply = 1
                left_side = 0.25 * multiply
                transprob4.append(left_side)
            elif item[0] > 0 and item[1] == 0 and item[3] > 0:
                multiply = 1
                left_side = 0.5 * multiply
                transprob4.append(left_side)
            elif item[0] > 0 and item[1] == 0 and item[3] == 0:
                multiply = 1
                left_side = 0.5 * multiply
                transprob4.append(left_side)
            elif item[0] == 0 and item[1] > 0 and item[3] > 0:
                multiply = 1
                left_side = 0.5 * multiply
                transprob4.append(left_side)
            elif item[0] == 0 and item[1] > 0 and item[3] == 0:
                multiply = 1
                left_side = 0.5 * multiply
                transprob4.append(left_side)
            elif item[0] == 0 and item[1] == 0 and item[3] > 0:
                multiply = 1
                left_side = 0 * multiply
                transprob4.append(left_side)
            elif item[0] == 0 and item[1] == 0 and item[3] == 0:
                multiply = 1
                left_side = 1 * multiply
                transprob4.append(left_side)
    return transprob4

def TP5():
    transdna5 = pinput.iloc[[4], [7]]
    multiply = 1
    left_side = 0
    transprob5 = [left_side]
    for item in binary:
        if item[4] == 0 and transdna5.values == 1:
            left_side = 0
            transprob5.append(left_side)
        else:
            if item[0] > 0 and item[1] > 0 and item[4] > 0:
                left_side = 0.75 * multiply
                transprob5.append(left_side)
            elif item[0] > 0 and item[1] > 0 and item[4] == 0:
                left_side = 0.25 * multiply
                transprob5.append(left_side)
            elif item[0] > 0 and item[1] == 0 and item[4] > 0:
                left_side = 0.5 * multiply
                transprob5.append(left_side)
            elif item[0] > 0 and item[1] == 0 and item[4] == 0:
                left_side = 0.5 * multiply
                transprob5.append(left_side)
            elif item[0] == 0 and item[1] > 0 and item[4] > 0:
                left_side = 0.5 * multiply
                transprob5.append(left_side)
            elif item[0] == 0 and item[1] > 0 and item[4] == 0:
                left_side = 0.5 * multiply
                transprob5.append(left_side)
            elif item[0] == 0 and item[1] == 0 and item[4] > 0:
                left_side = 0 * multiply
                transprob5.append(left_side)
            elif item[0] == 0 and item[1] == 0 and item[4] == 0:
                left_side = 1 * multiply
                transprob5.append(left_side)
    return transprob5

def TP6():
    transdna6 = pinput.iloc[[5], [7]]
    multiply = 1
    left_side = 0
    transprob6 = [left_side]
    for item in binary:
        if item[5] == 0 and transdna6.values == 1:
            left_side = 0
            transprob6.append(left_side)
        else:
            if item[0] > 0 and item[1] > 0 and item[5] > 0:
                left_side = 0.75 * multiply
                transprob6.append(left_side)
            elif item[0] > 0 and item[1] > 0 and item[5] == 0:
                left_side = 0.25 * multiply
                transprob6.append(left_side)
            elif item[0] > 0 and item[1] == 0 and item[5] > 0:
                left_side = 0.5 * multiply
                transprob6.append(left_side)
            elif item[0] > 0 and item[1] == 0 and item[5] == 0:
                left_side = 0.5 * multiply
                transprob6.append(left_side)
            elif item[0] == 0 and item[1] > 0 and item[5] > 0:
                left_side = 0.5 * multiply
                transprob6.append(left_side)
            elif item[0] == 0 and item[1] > 0 and item[5] == 0:
                left_side = 0.5 * multiply
                transprob6.append(left_side)
            elif item[0] == 0 and item[1] == 0 and item[5] > 0:
                left_side = 0 * multiply
                transprob6.append(left_side)
            elif item[0] == 0 and item[1] == 0 and item[5] == 0:
                left_side = 1 * multiply
                transprob6.append(left_side)
    return transprob6

def TP7():
    transdna7 = pinput.iloc[[6], [7]]
    multiply = 1
    left_side = 0
    transprob7 = [left_side]
    for item in binary:
        if item[6] == 0 and transdna7.values == 1:
            left_side = 0
            transprob7.append(left_side)
        else:
            if item[2] > 0 and item[5] > 0 and item[6] > 0:
                left_side = 0.75 * multiply
                transprob7.append(left_side)
            elif item[2] > 0 and item[5] > 0 and item[6] == 0:
                left_side = 0.25 * multiply
                transprob7.append(left_side)
            elif item[2] > 0 and item[5] == 0 and item[6] > 0:
                left_side = 0.5 * multiply
                transprob7.append(left_side)
            elif item[2] > 0 and item[5] == 0 and item[6] == 0:
                left_side = 0.5 * multiply
                transprob7.append(left_side)
            elif item[2] == 0 and item[5] > 0 and item[6] > 0:
                left_side = 0.5 * multiply
                transprob7.append(left_side)
            elif item[2] == 0 and item[5] > 0 and item[6] == 0:
                left_side = 0.5 * multiply
                transprob7.append(left_side)
            elif item[2] == 0 and item[5] == 0 and item[6] > 0:
                left_side = 0 * multiply
                transprob7.append(left_side)
            elif item[2] == 0 and item[5] == 0 and item[6] == 0:
                left_side = 1 * multiply
                transprob7.append(left_side)

    return transprob7

def TP8():
    transdna8 = pinput.iloc[[7], [7]]
    multiply = 1
    left_side = 0
    transprob8 = [left_side]
    for item in binary:
        if item[7] == 0 and transdna8.values == 1:
            left_side = 0
            transprob8.append(left_side)
        else:
            if item[2] > 0 and item[5] > 0 and item[7] > 0:
                left_side = 0.75 * multiply
                transprob8.append(left_side)
            elif item[2] > 0 and item[5] > 0 and item[7] == 0:
                left_side = 0.25 * multiply
                transprob8.append(left_side)
            elif item[2] > 0 and item[5] == 0 and item[7] > 0:
                left_side = 0.5 * multiply
                transprob8.append(left_side)
            elif item[2] > 0 and item[5] == 0 and item[7] == 0:
                left_side = 0.5 * multiply
                transprob8.append(left_side)
            elif item[2] == 0 and item[5] > 0 and item[7] > 0:
                left_side = 0.5 * multiply
                transprob8.append(left_side)
            elif item[2] == 0 and item[5] > 0 and item[7] == 0:
                left_side = 0.5 * multiply
                transprob8.append(left_side)
            elif item[2] == 0 and item[5] == 0 and item[7] > 0:
                left_side = 0 * multiply
                transprob8.append(left_side)
            elif item[2] == 0 and item[5] == 0 and item[7] == 0:
                left_side = 1 * multiply
                transprob8.append(left_side)

    return transprob8

def TP9():
    transdna9 = pinput.iloc[[8], [7]]
    multiply = 1
    left_side = 0
    transprob9 = [left_side]
    for item in binary:
        if item[8] == 0 and transdna9.values == 1:
            left_side = 0
            transprob9.append(left_side)
        else:
            if item[2] > 0 and item[5] > 0 and item[8] > 0:
                left_side = 0.75 * multiply
                transprob9.append(left_side)
            elif item[2] > 0 and item[5] > 0 and item[8] == 0:
                left_side = 0.25 * multiply
                transprob9.append(left_side)
            elif item[2] > 0 and item[5] == 0 and item[8] > 0:
                left_side = 0.5 * multiply
                transprob9.append(left_side)
            elif item[2] > 0 and item[5] == 0 and item[8] == 0:
                left_side = 0.5 * multiply
                transprob9.append(left_side)
            elif item[2] == 0 and item[5] > 0 and item[8] > 0:
                left_side = 0.5 * multiply
                transprob9.append(left_side)
            elif item[2] == 0 and item[5] > 0 and item[8] == 0:
                left_side = 0.5 * multiply
                transprob9.append(left_side)
            elif item[2] == 0 and item[5] == 0 and item[8] > 0:
                left_side = 0 * multiply
                transprob9.append(left_side)
            elif item[2] == 0 and item[5] == 0 and item[8] == 0:
                left_side = 1 * multiply
                transprob9.append(left_side)

    return transprob9

transmission = pd.DataFrame([TP4(), TP5(), TP6(), TP7(), TP8(), TP9()]).transpose()
transmissionprob = transmission.iloc[1:,:]

def LDLC1():
    ldlcage1 = pinput.iloc[0, 0]
    ldlccheck1 = pinput.iloc[0, 1]
    ldlctotalc1 = pinput.iloc[0, 2]
    isfh = ldlcfh(ldlcage1, ldlccheck1, ldlctotalc1)
    notfh = ldlcnotfh(ldlccheck1, ldlcage1, ldlctotalc1)
    ldlcprob = 0
    ldlcoutput = [ldlcprob]
    for item in binary:
        if item[0] == 0:
            ldlcprob = notfh
            ldlcoutput.append(ldlcprob)
        else:
            ldlcprob = isfh
            ldlcoutput.append(ldlcprob)
    return ldlcoutput

def LDLC2():
    ldlcage2 = pinput.iloc[1, 0]
    ldlccheck2 = pinput.iloc[1, 1]
    ldlctotalc2 = pinput.iloc[1, 2]
    isfh = ldlcfh(ldlcage2,ldlccheck2, ldlctotalc2)
    notfh = ldlcnotfh(ldlccheck2, ldlcage2, ldlctotalc2)
    ldlcprob = 0
    ldlcoutput = [ldlcprob]
    for item in binary:
        if item[1] == 0:
            ldlcprob = notfh
            ldlcoutput.append(ldlcprob)
        else:
            ldlcprob = isfh
            ldlcoutput.append(ldlcprob)
    return ldlcoutput

def LDLC3():
    ldlcage3 = pinput.iloc[2, 0]
    ldlccheck3 = pinput.iloc[2, 1]
    ldlctotalc3 = pinput.iloc[2, 2]
    isfh = ldlcfh(ldlcage3, ldlccheck3, ldlctotalc3)
    notfh = ldlcnotfh(ldlccheck3, ldlcage3, ldlctotalc3)
    ldlcprob = 0
    ldlcoutput = [ldlcprob]
    for item in binary:
        if item[2] == 0:
            ldlcprob = notfh
            ldlcoutput.append(ldlcprob)
        else:
            ldlcprob = isfh
            ldlcoutput.append(ldlcprob)
    return ldlcoutput

def LDLC4():
    ldlcage4 = pinput.iloc[3, 0]
    ldlccheck4 = pinput.iloc[3, 1]
    ldlctotalc4 = pinput.iloc[3, 2]
    isfh = ldlcfh(ldlcage4, ldlccheck4, ldlctotalc4)
    notfh = ldlcnotfh(ldlccheck4, ldlcage4, ldlctotalc4)
    ldlcprob = 0
    ldlcoutput = [ldlcprob]
    for item in binary:
        if item[3] == 0:
            ldlcprob = notfh
            ldlcoutput.append(ldlcprob)
        else:
            ldlcprob = isfh
            ldlcoutput.append(ldlcprob)
    return ldlcoutput

def LDLC5():
    ldlcage5 = pinput.iloc[4, 0]
    ldlccheck5 = pinput.iloc[4, 1]
    ldlctotalc5 = pinput.iloc[4, 2]
    isfh = ldlcfh(ldlcage5, ldlccheck5, ldlctotalc5)
    notfh = ldlcnotfh(ldlccheck5, ldlcage5, ldlctotalc5)
    ldlcprob = 0
    ldlcoutput = [ldlcprob]
    for item in binary:
        if item[4] == 0:
            ldlcprob = notfh
            ldlcoutput.append(ldlcprob)
        else:
            ldlcprob = isfh
            ldlcoutput.append(ldlcprob)
    return ldlcoutput

def LDLC6():
    ldlcage6 = pinput.iloc[5, 0]
    ldlccheck6 = pinput.iloc[5, 1]
    ldlctotalc6 = pinput.iloc[5, 2]
    isfh = ldlcfh(ldlcage6, ldlccheck6, ldlctotalc6)
    notfh = ldlcnotfh(ldlccheck6, ldlcage6, ldlctotalc6)
    ldlcprob = 0
    ldlcoutput = [ldlcprob]
    for item in binary:
        if item[5] == 0:
            ldlcprob = notfh
            ldlcoutput.append(ldlcprob)
        else:
            ldlcprob = isfh
            ldlcoutput.append(ldlcprob)
    return ldlcoutput

def LDLC7():
    ldlcage7 = pinput.iloc[6, 0]
    ldlccheck7 = pinput.iloc[6, 1]
    ldlctotalc7 = pinput.iloc[6, 2]
    isfh = ldlcfh(ldlcage7, ldlccheck7, ldlctotalc7)
    notfh = ldlcnotfh(ldlccheck7, ldlcage7, ldlctotalc7)
    ldlcprob = 0
    ldlcoutput = [ldlcprob]
    for item in binary:
        if item[6] == 0:
            ldlcprob = notfh
            ldlcoutput.append(ldlcprob)
        else:
            ldlcprob = isfh
            ldlcoutput.append(ldlcprob)
    return ldlcoutput

def LDLC8():
    ldlcage8 = pinput.iloc[7, 0]
    ldlccheck8 = pinput.iloc[7, 1]
    ldlctotalc8 = pinput.iloc[7, 2]
    isfh = ldlcfh(ldlcage8, ldlccheck8, ldlctotalc8)
    notfh = ldlcnotfh(ldlccheck8, ldlcage8, ldlctotalc8)
    ldlcprob = 0
    ldlcoutput = [ldlcprob]
    for item in binary:
        if item[7] == 0:
            ldlcprob = notfh
            ldlcoutput.append(ldlcprob)
        else:
            ldlcprob = isfh
            ldlcoutput.append(ldlcprob)
    return ldlcoutput

def LDLC9():
    ldlcage9 = pinput.iloc[8, 0]
    ldlccheck9 = pinput.iloc[8, 1]
    ldlctotalc9 = pinput.iloc[8, 2]
    isfh = ldlcfh(ldlcage9, ldlccheck9, ldlctotalc9)
    notfh = ldlcnotfh(ldlccheck9, ldlcage9, ldlctotalc9)
    ldlcprob = 0
    ldlcoutput = [ldlcprob]
    for item in binary:
        if item[8] == 0:
            ldlcprob = notfh
            ldlcoutput.append(ldlcprob)
        else:
            ldlcprob = isfh
            ldlcoutput.append(ldlcprob)
    return ldlcoutput
ldldf = pd.DataFrame([LDLC1(), LDLC2(), LDLC3(), LDLC4(), LDLC5(), LDLC6(), LDLC7(), LDLC8(), LDLC9()]).transpose()
ldlarray = ldldf.iloc[1:,:]
# print(ldlarray)


def TX1():
    tx1 = pinput.iloc[0, 6]
    txldlc1 = pinput.iloc[0, 1]
    txage1 = pinput.iloc[0, 0]
    istx = TXPFISFH(txldlc1, txage1, tx1)
    nottx = TXPFISNOTFH(tx1)
    txprob = 0
    txoutput = [txprob]
    for item in binary:
        if item[0] == 1:
            txprob = istx
            txoutput.append(txprob)
        else:
            txprob = nottx
            txoutput.append(txprob)
    return txoutput

def TX2():
    tx2 = pinput.iloc[1, 6]
    txldlc2 = pinput.iloc[1, 1]
    txage2 = pinput.iloc[1, 0]
    istx = TXPFISFH(txldlc2, txage2, tx2)
    nottx = TXPFISNOTFH(tx2)
    txprob = 0
    txoutput = [txprob]
    for item in binary:
        if item[1] == 1:
            txprob = istx
            txoutput.append(txprob)
        else:
            txprob = nottx
            txoutput.append(txprob)
    return txoutput

def TX3():
    tx3 = pinput.iloc[2, 6]
    txldlc3 = pinput.iloc[2, 1]
    txage3 = pinput.iloc[2, 0]
    istx = TXPFISFH(txldlc3, txage3, tx3)
    nottx = TXPFISNOTFH(tx3)
    txprob = 0
    txoutput = [txprob]
    for item in binary:
        if item[2] == 1:
            txprob = istx
            txoutput.append(txprob)
        else:
            txprob = nottx
            txoutput.append(txprob)
    return txoutput

def TX4():
    tx4 = pinput.iloc[3, 6]
    txldlc4 = pinput.iloc[3, 1]
    txage4 = pinput.iloc[3, 0]
    istx = TXPFISFH(txldlc4, txage4, tx4)
    nottx = TXPFISNOTFH(tx4)
    txprob = 0
    txoutput = [txprob]
    for item in binary:
        if item[3] == 1:
            txprob = istx
            txoutput.append(txprob)
        else:
            txprob = nottx
            txoutput.append(txprob)
    return txoutput

def TX5():
    tx5 = pinput.iloc[4, 6]
    txldlc5 = pinput.iloc[4, 1]
    txage5 = pinput.iloc[4, 0]
    istx = TXPFISFH(txldlc5, txage5, tx5)
    nottx = TXPFISNOTFH(tx5)
    txprob = 0
    txoutput = [txprob]
    for item in binary:
        if item[4] == 1:
            txprob = istx
            txoutput.append(txprob)
        else:
            txprob = nottx
            txoutput.append(txprob)
    return txoutput

def TX6():
    tx6 = pinput.iloc[5, 6]
    txldlc6 = pinput.iloc[5, 1]
    txage6 = pinput.iloc[5, 0]
    istx = TXPFISFH(txldlc6, txage6, tx6)
    nottx = TXPFISNOTFH(tx6)
    txprob = 0
    txoutput = [txprob]
    for item in binary:
        if item[5] == 1:
            txprob = istx
            txoutput.append(txprob)
        else:
            txprob = nottx
            txoutput.append(txprob)
    return txoutput

def TX7():
    tx7 = pinput.iloc[6, 6]
    txldlc7 = pinput.iloc[6, 1]
    txage7 = pinput.iloc[6, 0]
    istx = TXPFISFH(txldlc7, txage7, tx7)
    nottx = TXPFISNOTFH(tx7)
    txprob = 0
    txoutput = [txprob]
    for item in binary:
        if item[6] == 1:
            txprob = istx
            txoutput.append(txprob)
        else:
            txprob = nottx
            txoutput.append(txprob)
    return txoutput

def TX8():
    tx8 = pinput.iloc[7, 6]
    txldlc8 = pinput.iloc[7, 1]
    txage8 = pinput.iloc[7, 0]
    istx = TXPFISFH(txldlc8, txage8, tx8)
    nottx = TXPFISNOTFH(tx8)
    txprob = 0
    txoutput = [txprob]
    for item in binary:
        if item[7] == 1:
            txprob = istx
            txoutput.append(txprob)
        else:
            txprob = nottx
            txoutput.append(txprob)
    return txoutput

def TX9():
    tx9 = pinput.iloc[8, 6]
    txldlc9 = pinput.iloc[8, 1]
    txage9 = pinput.iloc[8, 0]
    istx = TXPFISFH(txldlc9, txage9, tx9)
    nottx = TXPFISNOTFH(tx9)
    txprob = 0
    txoutput = [txprob]
    for item in binary:
        if item[8] == 1:
            txprob = istx
            txoutput.append(txprob)
        else:
            txprob = nottx
            txoutput.append(txprob)
    return txoutput

txdf = pd.DataFrame([TX1(), TX2(), TX3(), TX4(), TX5(), TX6(), TX7(), TX8(), TX9()]).transpose()
txarray = txdf.iloc[1:,:]
# print(txarray)

def CAD1():
    cadclinical1 = pinput.iloc[0, 4]
    cadgender1 = pinput.iloc[0, 3]
    cadonsetage1 = pinput.iloc[0, 5]
    cadage1 = pinput.iloc[0, 0]
    iscad1 = CADPFISFH(cadclinical1, cadgender1, cadonsetage1, cadage1)
    isnotcad1 = CADISNOTFH(cadclinical1, cadgender1, cadonsetage1, cadage1)
    cadprob = 0
    cadoutput = [cadprob]
    for item in binary:
        if item[0] == 1:
            cadprob = iscad1
            cadoutput.append(cadprob)
        else:
            cadprob = isnotcad1
            cadoutput.append(cadprob)
    return cadoutput

def CAD2():
    cadclinical2 = pinput.iloc[1, 4]
    cadgender2 = pinput.iloc[1, 3]
    cadonsetage2 = pinput.iloc[1, 5]
    cadage2 = pinput.iloc[1, 0]
    iscad2 = CADPFISFH(cadclinical2, cadgender2, cadonsetage2, cadage2)
    isnotcad2 = CADISNOTFH(cadclinical2, cadgender2, cadonsetage2, cadage2)
    cadprob = 0
    cadoutput = [cadprob]
    for item in binary:
        if item[1] == 1:
            cadprob = iscad2
            cadoutput.append(cadprob)
        else:
            cadprob = isnotcad2
            cadoutput.append(cadprob)
    return cadoutput

def CAD3():
    cadclinical3 = pinput.iloc[2, 4]
    cadgender3 = pinput.iloc[2, 3]
    cadonsetage3 = pinput.iloc[2, 5]
    cadage3 = pinput.iloc[2, 0]
    iscad3 = CADPFISFH(cadclinical3, cadgender3, cadonsetage3, cadage3)
    isnotcad3 = CADISNOTFH(cadclinical3, cadgender3, cadonsetage3, cadage3)
    cadprob = 0
    cadoutput = [cadprob]
    for item in binary:
        if item[2] == 1:
            cadprob = iscad3
            cadoutput.append(cadprob)
        else:
            cadprob = isnotcad3
            cadoutput.append(cadprob)
    return cadoutput

def CAD4():
    cadclinical4 = pinput.iloc[3, 4]
    cadgender4 = pinput.iloc[3, 3]
    cadonsetage4 = pinput.iloc[3, 5]
    cadage4 = pinput.iloc[3, 0]
    iscad4 = CADPFISFH(cadclinical4, cadgender4, cadonsetage4, cadage4)
    isnotcad4 = CADISNOTFH(cadclinical4, cadgender4, cadonsetage4, cadage4)
    cadprob = 0
    cadoutput = [cadprob]
    for item in binary:
        if item[3] == 1:
            cadprob = iscad4
            cadoutput.append(cadprob)
        else:
            cadprob = isnotcad4
            cadoutput.append(cadprob)
    return cadoutput

def CAD5():
    cadclinical5 = pinput.iloc[4, 4]
    cadgender5 = pinput.iloc[4, 3]
    cadonsetage5 = pinput.iloc[4, 5]
    cadage5 = pinput.iloc[4, 0]
    iscad5 = CADPFISFH(cadclinical5, cadgender5, cadonsetage5, cadage5)
    isnotcad5 = CADISNOTFH(cadclinical5, cadgender5, cadonsetage5, cadage5)
    cadprob = 0
    cadoutput = [cadprob]
    for item in binary:
        if item[4] == 1:
            cadprob = iscad5
            cadoutput.append(cadprob)
        else:
            cadprob = isnotcad5
            cadoutput.append(cadprob)
    return cadoutput

def CAD6():
    cadclinical6 = pinput.iloc[5, 4]
    cadgender6 = pinput.iloc[5, 3]
    cadonsetage6 = pinput.iloc[5, 5]
    cadage6 = pinput.iloc[5, 0]
    iscad6 = CADPFISFH(cadclinical6, cadgender6, cadonsetage6, cadage6)
    isnotcad6 = CADISNOTFH(cadclinical6, cadgender6, cadonsetage6, cadage6)
    cadprob = 0
    cadoutput = [cadprob]
    for item in binary:
        if item[5] == 1:
            cadprob = iscad6
            cadoutput.append(cadprob)
        else:
            cadprob = isnotcad6
            cadoutput.append(cadprob)
    return cadoutput

def CAD7():
    cadclinical7 = pinput.iloc[6, 4]
    cadgender7 = pinput.iloc[6, 3]
    cadonsetage7 = pinput.iloc[6, 5]
    cadage7 = pinput.iloc[6, 0]
    iscad7 = CADPFISFH(cadclinical7, cadgender7, cadonsetage7, cadage7)
    isnotcad7 = CADISNOTFH(cadclinical7, cadgender7, cadonsetage7, cadage7)
    cadprob = 0
    cadoutput = [cadprob]
    for item in binary:
        if item[6] == 1:
            cadprob = iscad7
            cadoutput.append(cadprob)
        else:
            cadprob = isnotcad7
            cadoutput.append(cadprob)
    return cadoutput

def CAD8():
    cadclinical8 = pinput.iloc[7, 4]
    cadgender8 = pinput.iloc[7, 3]
    cadonsetage8 = pinput.iloc[7, 5]
    cadage8 = pinput.iloc[7, 0]
    iscad8 = CADPFISFH(cadclinical8, cadgender8, cadonsetage8, cadage8)
    isnotcad8 = CADISNOTFH(cadclinical8, cadgender8, cadonsetage8, cadage8)
    cadprob = 0
    cadoutput = [cadprob]
    for item in binary:
        if item[7] == 1:
            cadprob = iscad8
            cadoutput.append(cadprob)
        else:
            cadprob = isnotcad8
            cadoutput.append(cadprob)
    return cadoutput

def CAD9():
    cadclinical9 = pinput.iloc[8, 4]
    cadgender9 = pinput.iloc[8, 3]
    cadonsetage9 = pinput.iloc[8, 5]
    cadage9 = pinput.iloc[8, 0]
    iscad9 = CADPFISFH(cadclinical9, cadgender9, cadonsetage9, cadage9)
    isnotcad9 = CADISNOTFH(cadclinical9, cadgender9, cadonsetage9, cadage9)
    cadprob = 0
    cadoutput = [cadprob]
    for item in binary:
        if item[8] == 1:
            cadprob = iscad9
            cadoutput.append(cadprob)
        else:
            cadprob = isnotcad9
            cadoutput.append(cadprob)
    return cadoutput


caddf = pd.DataFrame([CAD1(), CAD2(), CAD3(), CAD4(), CAD5(), CAD6(), CAD7(), CAD8(), CAD9()]).transpose()
cadarray = caddf.iloc[1:,:]
# print(cadarray)

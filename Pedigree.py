# TODO() - Replicate Pedigree Person, but use OOP -- WILL THIS SPEED UP PROCESSING?
from scipy import stats
from flask import Flask
import math
import numpy as np
from itertools import product
import pandas as pd
import datetime

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
calc = 0

# Binary Table for 512 Pedigree Possibilities
binary = [i for i in product(range(2), repeat=9)]
binary = np.array(binary)

pinput = pd.DataFrame(
            columns=["Age", "LDL-C", "TOT-C", "Gender", "Clinical-CAD", "CAD-Age", "TX-Status", "DNA-DX Status"]
            , data=[[0, 0, 0, "f", 0, 0, 0, 0]
                , [0, 0, 0, "f", 0, 0, 0, 0]
                , [0, 0, 0, "f", 0, 0, 0, 0]
                , [0, 0, 0, "f", 0, 0, 0, 0]
                , [0, 0, 0, "f", 0, 0, 0, 0]
                , [0, 0, 0, "f", 0, 0, 0, 0]
                , [0, 0, 0, "f", 0, 0, 0, 0]
                , [0, 0, 0, "f", 0, 0, 0, 0]
                , [0, 0, 0, "f", 0, 0, 0, 0]])

class Person(object):
    def __init__(self, id, age, gender, ldlc, totc, txstatus, cadstatus, cadageonset, dnadx, fhprob):
        self.id = id
        self.pedigree_role = self.family_role()
        self.age = age
        self.gender = gender
        self.ldlc = ldlc
        self.totc = totc
        self.txstatus = txstatus
        self.cadstatus = cadstatus
        self.cadageonset = cadageonset
        self.dnadx = dnadx
        self.fhprob = fhprob
        self.ldlcfh = self.ldlcfh()
        self.ldlcnotfh = self.ldlcnotfh()
        self.txfh = self.txfh()
        self.txnotfh = self.txnotfh()
        self.cadfh = self.cadfh()
        self.cadnotfh = self.cadnotfh()

        ###############################################################
        # Handling the 0, 1, or 9 Inputs for tx, cadstatus, and dnadx #
        ###############################################################

        # Returning the Printed vals of TX Status
        if self.txstatus == 9:
            self.txstatus = "Unknown"
        elif self.txstatus == 1:
            self.txstatus = "Positive"
        elif self.txstatus == 0:
            self.txstatus = "Negative"
        else:
            pass

        if self.cadstatus == 9:
            self.cadstatus = "Unknown"
        elif self.cadstatus == 1:
            self.cadstatus = "Positive"
        elif self.cadstatus == 0:
            self.cadstatus = "Negative"
        else:
            pass

        if self.dnadx == 9:
            self.dnadx = "Unknown"
        elif self.dnadx == 1:
            self.dnadx = "Positive"
        elif self.dnadx == 0:
            self.dnadx = "Negative"
        else:
            pass

    # Returning the Pedigree Role
    def family_role(self):
        if self.id == 1:
            self.pedigree_role = "Grandparent 1"
            return self.pedigree_role

        elif self.id == 2:
            self.pedigree_role = "Grandparent 2"
            return self.pedigree_role

        elif self.id == 3:
            self.pedigree_role = "Parent 2"
            return self.pedigree_role

        elif self.id == 4:
            self.pedigree_role = "Sibling 1 of Parent 1"
            return self.pedigree_role

        elif self.id == 5:
            self.pedigree_role = "Sibling 2 of Parent 2"
            return self.pedigree_role

        elif self.id == 6:
            self.pedigree_role = "Parent 1"
            return self.pedigree_role

        elif self.id == 7:
            self.pedigree_role = "Child 1"
            return self.pedigree_role

        elif self.id == 8:
            self.pedigree_role = "Child 2"
            return self.pedigree_role

        elif self.id == 9:
            self.pedigree_role = "Child 3"
            return self.pedigree_role
    # LDL FH Val
    def ldlcfh(self):
        if self.ldlc == 0 and self.totc == 0:
            returnvar = 1
        else:
            value1 = 1
            if self.ldlc > 0:
                if self.age < 20:
                    meantrue = value1 * ldlcfhlessthan20mean
                    sdtrue = value1 * ldlcfhlessthan20sd
                    returnvar = stats.norm.pdf(self.ldlc, meantrue, sdtrue)
                elif 20 <= self.age < 30:
                    meantrue = value1 * ldlcfh2030mean
                    sdtrue = value1 * ldlcfh2030sd
                    returnvar = stats.norm.pdf(self.ldlc, meantrue, sdtrue)
                elif self.age >= 30:
                    meantrue = value1 * ldlcfh30plusmean
                    sdtrue = value1 * ldlcfh30plussd
                    returnvar = stats.norm.pdf(self.ldlc, meantrue, sdtrue)
                else:
                    returnvar = 1
            else:
                if self.age< 20:
                    meanfalse = value1 * totalcfhlessthan20mean
                    sdfalse = value1 * totalcfhlessthan20sd
                    returnvar = stats.norm.pdf(self.totc, meanfalse, sdfalse)
                elif 20 <= self.age < 30:
                    meanfalse = value1 * totalcfh2030mean
                    sdfalse = value1 * totalcfh2030sd
                    returnvar = stats.norm.pdf(self.totc, meanfalse, sdfalse)
                elif self.age >= 30:
                    meanfalse = value1 * totalcfh30plusmean
                    sdfalse = value1 * totalcfh30plussd
                    returnvar = stats.norm.pdf(self.totc, meanfalse, sdfalse)
                else:
                    returnvar = 1
        return returnvar

    # LDL Not FH Val
    def ldlcnotfh(self):
        if self.ldlc == 0 and self.totc == 0:
            returnvar = 1
        else:
            value1 = 1
            if self.ldlc > 0:
                if self.age < 20:
                    meantrue = value1 * ldlcnotfhlessthan20mean
                    sdtrue = value1 * ldlcnotfhlessthan20sd
                    returnvar = stats.norm.pdf(self.ldlc, meantrue, sdtrue)
                elif 20 <= self.age < 30:
                    meantrue = value1 * ldlcnotfh2030mean
                    sdtrue = value1 * ldlcnotfh2030sd
                    returnvar = stats.norm.pdf(self.ldlc, meantrue, sdtrue)
                elif self.age >= 30:
                    meantrue = value1 * ldlcnotfh30plusmean
                    sdtrue = value1 * ldlcnotfh30plussd
                    returnvar = stats.norm.pdf(self.ldlc, meantrue, sdtrue)
                else:
                    returnvar = 1
            else:
                if self.age< 20:
                    meanfalse = value1 * totalcnotfhlessthan20mean
                    sdfalse = value1 * totalcnotfhlessthan20sd
                    returnvar = stats.norm.pdf(self.totc, meanfalse, sdfalse)
                elif 20 <= self.age < 30:
                    meanfalse = value1 * totalcnotfh2030mean
                    sdfalse = value1 * totalcnotfh2030sd
                    returnvar = stats.norm.pdf(self.totc, meanfalse, sdfalse)
                elif self.age >= 30:
                    meanfalse = value1 * totalcnotfh30plusmean
                    sdfalse = value1 * totalcnotfh30plussd
                    returnvar = stats.norm.pdf(self.totc, meanfalse, sdfalse)
                else:
                    returnvar = 1
        return returnvar

    # TX FH Val
    def txfh(self):
            calc = 0
            if self.txstatus == 9:
                calc = 1
            else:
                if self.ldlc > 100:
                    calc = self.txstatus * ((0.8205 * self.age - 1.8113) / 100) + (1 - self.txstatus) * (1 - (0.8205 * self.age - 1.8113) / 100)
                else:
                    calc = self.txstatus * 1 + (1 - self.txstatus) * 1
            return calc

    # TX Not FH Val
    def txnotfh(self):
            calc = 0
            if self.txstatus == 9:
                calc = 1
            else:
                if self.txstatus == 1:
                    calc = 0.0001
                else:
                    calc = 1 - 0.0001
            return calc

    # CAD is FH
    def cadfh(self):
            calc = 0
            if self.cadstatus == 9:
                calc = 1
            else:
                if self.gender == "m":
                    if self.cadstatus == 1:
                        calc = 0.832 / (1 + math.exp(0.124 * (52.9 - self.cadageonset)))
                    else:
                        calc = 1 - (0.832 / (1 + math.exp(0.124 * (52.9 - self.age))))
                else:
                    if self.cadstatus == 1:
                        calc = 0.601 / (1 + math.exp(0.155 * (54.7 - self.cadageonset)))
                    else:
                        calc = 1 - (0.601 / (1 + math.exp(0.155 * (54.7 - self.age))))
            return calc

    # CAD is Not FH Val
    def cadnotfh(self):
            calc = 0
            if self.cadstatus == 9:
                calc = 1
            else:
                if self.gender == "m":
                    if self.cadstatus == 1:
                        calc = 0.499 / (1 + math.exp(0.142 * (69.6 - self.cadageonset)))
                    else:
                        calc = 1 - (0.499 / (1 + math.exp(0.142 * (69.6 - self.age))))
                else:
                    if self.cadstatus == 1:
                        calc = 0.713 / (1 + math.exp(0.0981 * (88.6 - self.cadageonset)))
                    else:
                        calc = 1 - (0.713 / (1 + math.exp(0.0981 * (88.6 - self.age))))
            return calc

# Grandparent 1
Grandparent_1 = Person( id = 1
                       , age = 72
                       , gender = "Male"
                       , ldlc = 200
                       , totc = 210
                       , txstatus = 0
                       , cadstatus = 9
                       , cadageonset = 0
                       , dnadx = 9
                       , fhprob = 0 )

# Grandparent 2
Grandparent_2 = Person(id = 2
                       , age = 73
                       , gender = "Female"
                       , ldlc = 190
                       , totc = 150
                       , txstatus = 9
                       , cadstatus = 9
                       , cadageonset = 0
                       , dnadx = 0
                       , fhprob = 0)

# Parent 2
Parent_2 = Person(id = 3
                  , age = 50
                  , gender = "Male"
                  , ldlc = 180
                  , totc = 170
                  , txstatus = 9
                  , cadstatus = 9
                  , cadageonset = 0
                  , dnadx = 9
                  , fhprob = 0)

# Sibling 1 of Parent 1
Sibling_1 = Person(id = 4
                   , age = 42
                   , gender = "Female"
                   , ldlc = 170
                   , totc = 190
                   , txstatus = 0
                   , cadstatus = 0
                   , cadageonset = 0
                   , dnadx = 0
                   , fhprob = 0)

# Sibling 2 of Parent 1
Sibling_2 = Person(id = 5
                   , age = 42
                   , gender = "Male"
                   , ldlc = 185
                   , totc = 199
                   , txstatus = 0
                   , cadstatus = 9
                   , cadageonset = 0
                   , dnadx = 9
                   , fhprob = 0)

# Parent 1
Parent_1 = Person(id = 6
                  , age = 48
                  , gender = "Female"
                  , ldlc = 160
                  , totc = 163
                  , txstatus = 9
                  , cadstatus = 0
                  , cadageonset = 0
                  , dnadx = 9
                  , fhprob = 0)

# Child 1
Child_1 = Person(id = 7
                 , age = 16
                 , gender = "Male"
                 , ldlc = 210
                 , totc = 232
                 , txstatus = 0
                 , cadstatus = 9
                 , cadageonset = 0
                 , dnadx = 9
                 , fhprob = 0)

# Child 2
Child_2 = Person(id = 8
                 , age = 20
                 , gender = "Male"
                 , ldlc = 225
                 , totc = 229
                 , txstatus = 1
                 , cadstatus = 9
                 , cadageonset = 0
                 , dnadx = 9
                 , fhprob = 0)

# Child 3
Child_3 = Person(id = 9
                 , age = 22
                 , gender = "Male"
                 , ldlc = 230
                 , totc = 232
                 , txstatus = 9
                 , cadstatus = 0
                 , cadageonset = 0
                 , dnadx = 0
                 , fhprob = 0)


for attr, value in Grandparent_1.__dict__.items():
    print(str(attr) + ": ", value)
print()

for attr, value in Grandparent_2.__dict__.items():
    print(str(attr) + ": ", value)
print()

for attr, value in Parent_1.__dict__.items():
    print(str(attr) + ": ", value)
print()

for attr, value in Sibling_1.__dict__.items():
    print(str(attr) + ": ", value)
print()

for attr, value in Sibling_2.__dict__.items():
    print(str(attr) + ": ", value)
print()

for attr, value in Parent_2.__dict__.items():
    print(str(attr) + ": ", value)
print()

for attr, value in Child_1.__dict__.items():
    print(str(attr) + ": ", value)
print()

for attr, value in Child_2.__dict__.items():
    print(str(attr) + ": ", value)
print()

for attr, value in Child_3.__dict__.items():
    print(str(attr) + ": ", value)
print()
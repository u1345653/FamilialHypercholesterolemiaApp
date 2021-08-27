from scipy import stats
from CAD import CADPFISFH
from CAD import CADISNOTFH
from TX import TXPFISNOTFH
from TX import TXPFISFH
age = int(input("Please enter your Age: "))
ldlc = int(input("Please enter you LDL-C Level: "))
totalc = int(input("Please enter your Total-C Level: "))
clinicalCAD = int(input("Does someone have clinical CAD: "))
gender = input("Please enter a gender ").lower()
onsetAge = int(input("PLease enter CAD onset age: "))
tx = int(input("Does someone have Tandon Xanthoma: "))
calc = 0
value1 = 0
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

def ldlcfh(x,y):
    if ldlc > 0:
        if age < 20:
            value1 = 1
            meantrue = value1 * ldlcfhlessthan20mean
            sdtrue = value1 * ldlcfhlessthan20sd
            return print(stats.norm.pdf(ldlc, meantrue, sdtrue))
        elif 20 <= age < 30:
            value1 = 1
            meantrue = value1 * ldlcfh2030mean
            sdtrue = value1 * ldlcfh2030sd
            return print(stats.norm.pdf(ldlc, meantrue, sdtrue))
        elif age >= 30:
            value1 = 1
            meantrue = value1 * ldlcfh30plusmean
            sdtrue = value1 * ldlcfh30plussd
            return print(stats.norm.pdf(ldlc, meantrue, sdtrue))
        else:
            value1 = 1
            return value1
    else:
        if age < 20:
            value1 = 1
            meanfalse = value1 * totalcfhlessthan20mean
            sdfalse = value1 * totalcfhlessthan20sd
            return print(stats.norm.pdf(totalc, meanfalse, sdfalse))
        elif 20 <= age < 30:
            value1 = 1
            meanfalse = value1 * totalcfh2030mean
            sdfalse = value1 * totalcfh2030sd
            return print(stats.norm.pdf(totalc, meanfalse, sdfalse))
        elif age >= 30:
            value1 = 1
            meanfalse = value1 * totalcfh30plusmean
            sdfalse = value1 * totalcfh30plussd
            return print(stats.norm.pdf(totalc, meanfalse, sdfalse))
        else:
            value1 = 1
            return value1

def ldlcnotfh(x,y):
    if ldlc > 0:
        if age < 20:
            value1 = 1
            meantrue = value1 * ldlcnotfhlessthan20mean
            sdtrue = value1 * ldlcnotfhlessthan20sd
            return print(stats.norm.pdf(ldlc, meantrue, sdtrue))
        elif 20 <= age < 30:
            value1 = 1
            meantrue = value1 * ldlcnotfh2030mean
            sdtrue = value1 * ldlcnotfh2030sd
            return print(stats.norm.pdf(ldlc, meantrue, sdtrue))
        elif age >= 30:
            value1 = 1
            meantrue = value1 * ldlcnotfh30plusmean
            sdtrue = value1 * ldlcnotfh30plussd
            return print(stats.norm.pdf(ldlc, meantrue, sdtrue))
        else:
            value1 = 1
            return value1
    else:
        if age < 20:
            value1 = 1
            meanfalse = value1 * totalcnotfhlessthan20mean
            sdfalse = value1 * totalcnotfhlessthan20sd
            return print(stats.norm.pdf(totalc, meanfalse, sdfalse))
        elif 20 <= age < 30:
            value1 = 1
            meanfalse = value1 * totalcnotfh2030mean
            sdfalse = value1 * totalcnotfh2030sd
            return print(stats.norm.pdf(totalc, meanfalse, sdfalse))
        elif age >= 30:
            value1 = 1
            meanfalse = value1 * totalcnotfh30plusmean
            sdfalse = value1 * totalcnotfh30plussd
            return print(stats.norm.pdf(totalc, meanfalse, sdfalse))
        else:
            value1 = 1
            return value1


print("LDL-C or total-C, CAD, and TX FH Percent:")
ldlcfh(age, ldlc)
CADPFISFH(clinicalCAD, gender, onsetAge, age)
TXPFISFH(ldlc, age, tx)
print("LDL-C or total-C, CAD, and TX Not FH Percent:")
ldlcnotfh(age, ldlc)
CADISNOTFH(clinicalCAD, gender, onsetAge, age)
TXPFISNOTFH(ldlc, age, tx)

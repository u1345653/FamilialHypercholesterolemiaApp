from scipy import stats
import math

age = int(input("Please enter your Age: "))
ldlc = int(input("Please enter you LDL-C Level: "))
totalc = int(input("Please enter your Total-C Level: "))
clinicalCAD = int(input("Does someone have clinical CAD: "))
gender = input("Please enter a gender ").lower()
onsetAge = int(input("Please enter CAD onset age: "))
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
returnvar = 0


def ldlcfh(x,y):
    if ldlc > 0:
        if age < 20:
            value1 = 1
            meantrue = value1 * ldlcfhlessthan20mean
            sdtrue = value1 * ldlcfhlessthan20sd
            returnvar = stats.norm.pdf(ldlc, meantrue, sdtrue)
            print(returnvar)
            return returnvar
        elif 20 <= age < 30:
            value1 = 1
            meantrue = value1 * ldlcfh2030mean
            sdtrue = value1 * ldlcfh2030sd
            returnvar = stats.norm.pdf(ldlc, meantrue, sdtrue)
            print(returnvar)
            return returnvar
        elif age >= 30:
            value1 = 1
            meantrue = value1 * ldlcfh30plusmean
            sdtrue = value1 * ldlcfh30plussd
            returnvar = stats.norm.pdf(ldlc, meantrue, sdtrue)
            print(returnvar)
            return returnvar
        else:
            value1 = 1
            return value1
    else:
        if age < 20:
            value1 = 1
            meanfalse = value1 * totalcfhlessthan20mean
            sdfalse = value1 * totalcfhlessthan20sd
            returnvar = stats.norm.pdf(totalc, meanfalse, sdfalse)
            print(returnvar)
            return returnvar
        elif 20 <= age < 30:
            value1 = 1
            meanfalse = value1 * totalcfh2030mean
            sdfalse = value1 * totalcfh2030sd
            returnvar = stats.norm.pdf(totalc, meanfalse, sdfalse)
            print(returnvar)
            return returnvar
        elif age >= 30:
            value1 = 1
            meanfalse = value1 * totalcfh30plusmean
            sdfalse = value1 * totalcfh30plussd
            returnvar = stats.norm.pdf(totalc, meanfalse, sdfalse)
            print(returnvar)
            return returnvar
        else:
            value1 = 1
            return value1

def ldlcnotfh(x,y):
    if ldlc > 0:
        if age < 20:
            value1 = 1
            meantrue = value1 * ldlcnotfhlessthan20mean
            sdtrue = value1 * ldlcnotfhlessthan20sd
            returnvar = stats.norm.pdf(ldlc, meantrue, sdtrue)
            print(returnvar)
            return returnvar
        elif 20 <= age < 30:
            value1 = 1
            meantrue = value1 * ldlcnotfh2030mean
            sdtrue = value1 * ldlcnotfh2030sd
            returnvar = stats.norm.pdf(ldlc, meantrue, sdtrue)
            print(returnvar)
            return returnvar
        elif age >= 30:
            value1 = 1
            meantrue = value1 * ldlcnotfh30plusmean
            sdtrue = value1 * ldlcnotfh30plussd
            returnvar = stats.norm.pdf(ldlc, meantrue, sdtrue)
            print(returnvar)
            return returnvar
        else:
            value1 = 1
            return value1
    else:
        if age < 20:
            value1 = 1
            meanfalse = value1 * totalcnotfhlessthan20mean
            sdfalse = value1 * totalcnotfhlessthan20sd
            returnvar = stats.norm.pdf(totalc, meanfalse, sdfalse)
            print(returnvar)
            return returnvar
        elif 20 <= age < 30:
            value1 = 1
            meanfalse = value1 * totalcnotfh2030mean
            sdfalse = value1 * totalcnotfh2030sd
            returnvar = stats.norm.pdf(totalc, meanfalse, sdfalse)
            print(returnvar)
            return returnvar
        elif age >= 30:
            value1 = 1
            meanfalse = value1 * totalcnotfh30plusmean
            sdfalse = value1 * totalcnotfh30plussd
            returnvar = stats.norm.pdf(totalc, meanfalse, sdfalse)
            print(returnvar)
            return returnvar
        else:
            value1 = 1
            return value1

def TXPFISFH(x,y,z):
    if tx == 9:
        calc = 1
        print(calc)
        return calc
    else:
        if ldlc >= 100:
            calc = tx * ((0.8205 * age-1.8113)/100) + (1-tx) * (1-(0.8205 * age - 1.8113)/100)
            print(calc)
            return calc
        elif ldlc < 100:
            calc = 1
            print(calc)
            return calc


def TXPFISNOTFH(x,y,z):
    if tx == 9:
        calc = 1
        print(calc)
        return calc
    else:
        if tx == 1:
            calc = 0.0001
            print(calc)
            return calc
        elif tx == 0:
            calc = 1 - 0.0001
            print(calc)
            return calc

def CADPFISFH(x,y,z,a):
    if clinicalCAD == 9:
        calc = 1
        print(calc)
        return calc
    else:
        if gender == "m":
            if clinicalCAD == 1:
                calc = 0.832/(1+math.exp(0.124*(52.9-onsetAge)))
                print(calc)
                return calc
            else:
                calc = 1 - (0.832/(1+math.exp(0.124*(52.9-age))))
                print(calc)
                return calc
        elif gender != "m":
            if clinicalCAD == 1:
                calc = 0.601/(1+math.exp(0.155*(54.7-onsetAge)))
                print(calc)
                return calc
            else:
                calc = 1-(0.601/(1+math.exp(0.155*(54.7-age))))
                print(calc)
                return calc


def CADISNOTFH(x,y,z,a):
    if clinicalCAD == 9:
        calc = 1
        print(calc)
        return calc
    else:
        if gender == "m":
            if clinicalCAD == 1:
                calc = 0.499/(1 + math.exp(0.142*(69.6-onsetAge)))
                print(calc)
                return calc
            else:
                calc = 1-(0.499/(1+math.exp(0.142*(69.6-age))))
                print(calc)
                return calc
        if gender != "m":
            if clinicalCAD == 1:
                calc = 0.713/(1+math.exp(0.0981*(88.6-onsetAge)))
                print(calc)
                return calc
            else:
                calc = 1-(0.713/(1+math.exp(0.0981*(88.6-age))))
                print(calc)
                return calc

print("LDL-C or total-C, CAD, and TX FH Percent:")
ldlcfh(age, ldlc)
TXPFISFH(ldlc, age, tx)
CADPFISFH(clinicalCAD, gender, onsetAge, age)

print("LDL-C or total-C, CAD, and TX Not FH Percent:")
ldlcnotfh(age, ldlc)
TXPFISNOTFH(ldlc, age, tx)
CADISNOTFH(clinicalCAD, gender, onsetAge, age)

import math


clinicalCAD = int(input("Does someone have clinical CAD: "))
gender = input("Please enter a gender ").lower()
onsetAge = int(input("PLease enter CAD onset age: "))
age = int(input("Please enter patient age "))
calc = 0


def CADPFISFH(x,y,z,a):
    if clinicalCAD == 9:
        calc = 1
        return print(calc)
    else:
        if gender == "m":
            if clinicalCAD == 1:
                calc = 0.832/(1+math.exp(0.124*(52.9-onsetAge)))
                return print(calc)
            else:
                calc = 1 - (0.832/(1+math.exp(0.124*(52.9-age))))
                return print(calc)
        elif gender != "m":
            if clinicalCAD == 1:
                calc = 0.601/(1+math.exp(0.155*(54.7-onsetAge)))
                return print(calc)
            else:
                calc = 1-(0.601/(1+math.exp(0.155*(54.7-age))))
                return print(calc)


def CADISNOTFH(x,y,z,a):
    if clinicalCAD == 9:
        calc = 1
        return print(calc)
    else:
        if gender == "m":
            if clinicalCAD == 1:
                calc = 0.499/(1 + math.exp(0.142*(69.6-onsetAge)))
                return print(calc)
            else:
                calc = 1-(0.499/(1+math.exp(0.142*(69.6-age))))
                return print(calc)
        if gender != "m":
            if clinicalCAD == 1:
                calc = 0.713/(1+math.exp(0.0981*(88.6-onsetAge)))
                return print(calc)
            else:
                calc = 1-(0.713/(1+math.exp(0.0981*(88.6-age))))
                return print(calc)

CADPFISFH(clinicalCAD, gender, onsetAge, age)
CADISNOTFH(clinicalCAD, gender, onsetAge, age)


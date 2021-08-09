age = int(input("Please enter an age: "))
ldlc = int(input("Please enter an ldlc level: "))
tx = int(input("Does someone have Tandon Xanthoma: "))
calc = 0


def TXPFISFH(x,y,z):
    if tx == 9:
        calc = 1
        return print(calc)
    else:
        if ldlc >= 100:
            calc = tx * ((0.8205 * age-1.8113)/100) + (1-tx) * (1-(0.8205 * age - 1.8113)/100)
            return print(calc)
        elif ldlc < 100:
            calc = 1
            return print(calc)


def TXPFISNOTFH(x,y,z):
    if tx == 9:
        calc = 1
        return print(calc)
    else:
        if tx == 1:
            calc = 0.0001
            return print(calc)
        elif tx == 0:
            calc = 1 - 0.0001
            return print(calc)

TXPFISFH(ldlc, age, tx)
TXPFISNOTFH(ldlc, age, tx)

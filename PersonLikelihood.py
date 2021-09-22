from Penetrance import binary
import StringLiklihood
import pandas as pd

x = binary
string = StringLiklihood.stringlike

def person1():
    value = 0
    output = [value]
    for item in x:
        if item[0] == 1:
            value = 1
            output.append(value)
        else:
            value = 0
            output.append(value)
    return output

person1f = pd.DataFrame([person1()]).transpose()
person1df = person1f.iloc[1:,:]
person1likely = person1df.mul(string.values)
person1likely.columns = ["Person 1 Likelihood"]
person1sum = pd.DataFrame([person1likely["Person 1 Likelihood"].sum()])
# print(person1df)
# print(person1likely)
# print(person1sum)

def person2():
    value = 0
    output = [value]
    for item in x:
        if item[1] == 1:
            value = 1
            output.append(value)
        else:
            value = 0
            output.append(value)
    return output

person2f = pd.DataFrame([person2()]).transpose()
person2df = person2f.iloc[1:,:]
person2likely = person2df.mul(string.values)
person2likely.columns = ["Person 2 Likelihood"]
person2sum = pd.DataFrame([person2likely["Person 2 Likelihood"].sum()])
# print(person2df)
# print(person2likely)
# print(person2sum)

def person3():
    value = 0
    output = [value]
    for item in x:
        if item[2] == 1:
            value = 1
            output.append(value)
        else:
            value = 0
            output.append(value)
    return output

person3f = pd.DataFrame([person3()]).transpose()
person3df = person3f.iloc[1:,:]
person3likely = person3df.mul(string.values)
person3likely.columns = ["Person 3 Likelihood"]
person3sum = pd.DataFrame([person3likely["Person 3 Likelihood"].sum()])
# print(person3df)
# print(person3likely)
# print(person3sum)

def person4():
    value = 0
    output = [value]
    for item in x:
        if item[3] == 1:
            value = 1
            output.append(value)
        else:
            value = 0
            output.append(value)
    return output

person4f = pd.DataFrame([person4()]).transpose()
person4df = person4f.iloc[1:,:]
person4likely = person4df.mul(string.values)
person4likely.columns = ["Person 4 Likelihood"]
person4sum = pd.DataFrame([person4likely["Person 4 Likelihood"].sum()])
# print(person4df)
# print(person4likely)
# print(person4sum)


def person5():
    value = 0
    output = [value]
    for item in x:
        if item[4] == 1:
            value = 1
            output.append(value)
        else:
            value = 0
            output.append(value)
    return output

person5f = pd.DataFrame([person5()]).transpose()
person5df = person5f.iloc[1:,:]
person5likely = person5df.mul(string.values)
person5likely.columns = ["Person 5 Likelihood"]
person5sum = pd.DataFrame([person5likely["Person 5 Likelihood"].sum()])
# print(person5df)
# print(person5likely)
# print(person5sum)

def person6():
    value = 0
    output = [value]
    for item in x:
        if item[5] == 1:
            value = 1
            output.append(value)
        else:
            value = 0
            output.append(value)
    return output

person6f = pd.DataFrame([person6()]).transpose()
person6df = person6f.iloc[1:,:]
person6likely = person6df.mul(string.values)
person6likely.columns = ["Person 6 Likelihood"]
person6sum = pd.DataFrame([person6likely["Person 6 Likelihood"].sum()])
# print(person6df)
# print(person6likely)
# print(person6sum)

def person7():
    value = 0
    output = [value]
    for item in x:
        if item[6] == 1:
            value = 1
            output.append(value)
        else:
            value = 0
            output.append(value)
    return output

person7f = pd.DataFrame([person7()]).transpose()
person7df = person7f.iloc[1:,:]
person7likely = person7df.mul(string.values)
person7likely.columns = ["Person 7 Likelihood"]
person7sum = pd.DataFrame([person7likely["Person 7 Likelihood"].sum()])
# print(person7df)
# print(person7likely)
# print(person7sum)

def person8():
    value = 0
    output = [value]
    for item in x:
        if item[7] == 1:
            value = 1
            output.append(value)
        else:
            value = 0
            output.append(value)
    return output

person8f = pd.DataFrame([person8()]).transpose()
person8df = person8f.iloc[1:,:]
person8likely = person8df.mul(string.values)
person8likely.columns = ["Person 8 Likelihood"]
person8sum = pd.DataFrame([person8likely["Person 8 Likelihood"].sum()])
# print(person8df)
# print(person8likely)
# print(person8sum)

def person9():
    value = 0
    output = [value]
    for item in x:
        if item[8] == 1:
            value = 1
            output.append(value)
        else:
            value = 0
            output.append(value)
    return output

person9f = pd.DataFrame([person9()]).transpose()
person9df = person9f.iloc[1:,:]
person9likely = person9df.mul(string.values)
person9likely.columns = ["Person 9 Likelihood"]
person9sum = pd.DataFrame([person9likely["Person 9 Likelihood"].sum()])
# print(person9df)
# print(person9likely)
# print(person9sum)


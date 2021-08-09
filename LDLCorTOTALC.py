from scipy import stats
from scipy.stats import norm
import numpy as nm

age = int(input("Please enter your Age: "))
ldlc = int(input("Please enter you LDL-C Level: "))
totalc = int(input("Please enter your Total-C Level: "))
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
value1 = 0
value2 = 175
value3 = 0


class Penatrance:

    def attempt2(x, y, z):
        if ldlc == 0 and totalc == 0:
            value1 = 1
            return print(value1)
        else:
            if ldlc > 0:
                value1 = stats.norm.cdf(ldlc, normdistmeantrue(age), normdistsdtrue(age))
                return print(value1)
            else:
                value1 = stats.norm.cdf(totalc, normdistmeanfalse(age), normdistsdfalse(age))
                return print(value1)
    def normdistmeantrue(x):
        if age < 20:
            value1 = 1
            value2 = value1 * ldlcfhlessthan20mean
            return print(value1,"age is less than 20", value2)
        elif 20 <= age < 30:
            value1 = 1
            value2 = value1 * ldlcfh2030mean
            return print(value1,"age is between 20 and 30", value2)
        elif age >= 30:
            value1 = 1
            value2 = value1 * ldlcfh30plusmean
            return print(value1,"Age is 30 or greater", value2)
        else:
            value1 = 1
            return value1
    def normdistsdtrue(x):
        if age < 20:
            value1 = 1
            value2 = value1 * ldlcfhlessthan20sd
            return print(value1,"age is less than 20", value2)
        elif 20 <= age < 30:
            value1 = 1
            value2 = value1 * ldlcfh2030sd
            return print(value1,"age is between 20 and 30", value2)
        elif age >= 30:
            value1 = 1
            value2 = value1 * ldlcfh30plussd
            return print(value1,"Age is 30 or greater", value2)
        else:
            value1 = 1
            return value1
    def normdistmeanfalse(x):
        if age < 20:
            value1 = 1
            value2 = value1 * totalcfhlessthan20mean
            return print(value1,"age is less than 20", value2)
        elif 20 <= age < 30:
            value1 = 1
            value2 = value1 * totalcfh2030mean
            return print(value1,"age is between 20 and 30", value2)
        elif age >= 30:
            value1 = 1
            value2 = value1 * totalcfh30plusmean
            return print(value1,"Age is 30 or greater", value2)
        else:
            value1 = 1
            return value1
    def normdistsdfalse(x):
        if age < 20:
            value1 = 1
            value2 = value1 * totalcfhlessthan20sd
            return print(value1,"age is less than 20", value2)
        elif 20 <= age < 30:
            value1 = 1
            value2 = value1 * totalcfh2030sd
            return print(value1,"age is between 20 and 30", value2)
        elif age >= 30:
            value1 = 1
            value2 = value1 * totalcfh30plussd
            return print(value1,"Age is 30 or greater", value2)
        else:
            value1 = 1
            return value1


# print(stats.norm.cdf(ldlc, (1*121), (1*35)))
# print(norm.sf(ldlc, (1*222), (1*76)))
#
# print(nm.random.normal(ldlc,(1*222), (1*76)))

attempt2(age, ldlc, totalc)


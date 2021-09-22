from Penetrance import binary
import StringLiklihood
import pandas as pd

likely = binary
string = StringLiklihood.stringlike

def family():
    value = 0
    output = [value]
    for row in likely:
        if row.any() == 1:
            value = 1
            output.append(value)
        elif row.any() == 0:
            value = 0
            output.append(value)
    return output

fam1 = pd.DataFrame([family()]).transpose()
fam = fam1.iloc[1:,:]
familylikelihood = fam.mul(string.values)
familylikelihood.columns = ["Family Likelihood"]
famsum = pd.DataFrame([familylikelihood["Family Likelihood"].sum()])
# print(famsum)


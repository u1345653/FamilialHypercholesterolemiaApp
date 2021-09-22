import StringLiklihood
import FamilyLikelihood
import PersonLikelihood

# Likelihood Results
person1prob = PersonLikelihood.person1sum.div(StringLiklihood.stringsum) * 100
print(f"Person 1 Likelihood: {person1prob.iloc[0, 0]}%")

person2prob = PersonLikelihood.person2sum.div(StringLiklihood.stringsum) * 100
print(f"Person 2 Likelihood: {person2prob.iloc[0, 0]}%")

person3prob = PersonLikelihood.person3sum.div(StringLiklihood.stringsum) * 100
print(f"Person 3 Likelihood: {person3prob.iloc[0, 0]}%")

person4prob = PersonLikelihood.person4sum.div(StringLiklihood.stringsum) * 100
print(f"Person 4 Likelihood: {person4prob.iloc[0, 0]}%")

person5prob = PersonLikelihood.person5sum.div(StringLiklihood.stringsum) * 100
print(f"Person 5 Likelihood: {person5prob.iloc[0, 0]}%")

person6prob = PersonLikelihood.person6sum.div(StringLiklihood.stringsum) * 100
print(f"Person 6 Likelihood: {person6prob.iloc[0, 0]}%")

person7prob = PersonLikelihood.person7sum.div(StringLiklihood.stringsum) * 100
print(f"Person 7 Likelihood: {person7prob.iloc[0, 0]}%")

person8prob = PersonLikelihood.person8sum.div(StringLiklihood.stringsum) * 100
print(f"Person 8 Likelihood: {person8prob.iloc[0, 0]}%")

person9prob = PersonLikelihood.person9sum.div(StringLiklihood.stringsum) * 100
print(f"Person 9 Likelihood: {person9prob.iloc[0, 0]}%")

familyprob = FamilyLikelihood.famsum.div(StringLiklihood.stringsum) * 100
print(f"Family Likelihood: {familyprob.iloc[0, 0]}%")

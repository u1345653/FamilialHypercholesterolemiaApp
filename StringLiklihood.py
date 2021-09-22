import pandas as pd
import Penetrance as P
pd.set_option('display.max_rows', None)
pd.set_option("display.max_columns", None)

probs = pd.DataFrame([P.FPP1(), P.FPP2(), P.FPP3(), P.TP4(), P.TP5(), P.TP6(), P.TP7(), P.TP8(), P.TP9(), P.LDLC1(), P.LDLC2(), P.LDLC3(), P.LDLC4(), P.LDLC5(), P.LDLC6(), P.LDLC7(),
                      P.LDLC8(), P.LDLC9(), P.TX1(), P.TX2(), P.TX3(), P.TX4(), P.TX5(), P.TX6(), P.TX7(), P.TX8(), P.TX9(), P.CAD1(), P.CAD2(), P.CAD3(), P.CAD4(), P.CAD5(), P.CAD6(),
                      P.CAD7(), P.CAD8(), P.CAD9()]).transpose()

#Creating 4 sections
section1 = pd.DataFrame([P.FPP1(), P.FPP2(), P.FPP3(), P.TP4(), P.TP5(), P.TP6(), P.TP7(), P.TP8(), P.TP9()]).transpose()
section2 = pd.DataFrame([P.LDLC1(), P.LDLC2(), P.LDLC3(), P.LDLC4(), P.LDLC5(), P.LDLC6(), P.LDLC7(), P.LDLC8(), P.LDLC9()]).transpose()
section3 = pd.DataFrame([P.TX1(), P.TX2(), P.TX3(), P.TX4(), P.TX5(), P.TX6(), P.TX7(), P.TX8(), P.TX9()]).transpose()
section4 = pd.DataFrame([P.CAD1(), P.CAD2(), P.CAD3(), P.CAD4(), P.CAD5(), P.CAD6(), P.CAD7(), P.CAD8(), P.CAD9()]).transpose()
# print(f"This is Section 1 {section1}")
# print(f"This is Section 2 {section2}")
# print(f"This is Section 3 {section3}")
# print(f"This is Section 4 {section4}")

#Creating products of 4 sections
section1prod = section1.prod(axis=1)
section2prod = section2.prod(axis=1)
section3prod = section3.prod(axis=1)
section4prod = section4.prod(axis=1)
# print(f"This is the start of section 1 product {section1prod}")
# print(f"This is the start of section 2 product {section2prod}")
# print(f"This is the start of section 3 product {section3prod}")
# print(f"This is the start of section 4 product {section4prod}")

#Creating 1 dataframe with the products of 4 sections
ultimateprod = pd.DataFrame([section1prod, section2prod, section3prod, section4prod]).transpose()
# print(f"This is the start of Ultimate Product {ultimateprod}")

#In the excel it is broken down into 4 section and uses the PRODUCT() function which multiples the areas in the section first, then the 4 sections.
#Mine is just multiplying all of the rows at once, I need to break it down to FPP1 - TP9, LDLC1-LDLC9, TX1-TX9, CAD1-CAD9 and multiply those results by eachother.
#How?
probs["String Likelihood"] = ultimateprod.prod(axis=1)
# print(probs)
string = probs.iloc[1:,:]
# print(string)
stringlike = pd.DataFrame([string["String Likelihood"]]).transpose()
# print(stringlike)
stringsum = pd.DataFrame([string["String Likelihood"].sum()])
#
# print(stringsum)



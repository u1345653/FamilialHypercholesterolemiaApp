"""
    Web-App changes to make post-discussion w/ Capstone-project Business Sponsor

    TO do's are Categorized by level of confidence in ability to make desired web page modification

    Most Important:

    Not 100% Confident that change will be Quick:
    TODO() - Keep values user input into form, after user generates results -- form vals get reset after submission

    Table-output Investigation
    TODO() - Vals not entered by user should display as '-' after submitting results, rather than '0' or 'f' for gender
    TODO() - Upon user changing any form-data, entire table populates w/ default vals....
        we want it to only update the corresponding cell in table ONLY! IS IT A JAVASCRIPT/JQuery thing?

    Non-important questions/items to consider or Solve for:
    TODO() - How can the calculation take less time on the backend to produce output on page quicker?
        Do we need to reconfigure calc.py to import the pedigree-algorithm as a separate .py module,
            rather than in calc.py?
        Instead of calculating everything in live-time, should we configure calc.py to pull from a preset db,
            which we then query from for algorithm inputs...?
            Does jQuery or JavaScript play a role in the page delay?

    TODO() - Why does the 'Download' feature not work when launching at pythoneverywhere.com server?
        Do we need to consider Heroku?

    TODO() - Consider adding option for user to upload .csv file, which serves as the algorithm inputs.

    TODO() - Consider re-configuring HTML-table to allow a user to click in cell & input value, rather than just
        displaying results of form-input.

    TODO() - Should we consider making the .jpg image of family pedigree responsive, allowing user to click on family
        member in-picture, then the form updating to pull-up that members data-inputs? Is it worth time required?
"""
from flask import render_template, request, url_for, jsonify, send_file
from scipy import stats
from flask import Flask
import math
import numpy as np
from itertools import product
import pandas as pd
import datetime
pd.set_option('display.max_rows', None)
pd.set_option("display.max_columns", None)
pd.set_option('precision', 0)

app = Flask(__name__)

#Create a Binary table
binary = [i for i in product(range(2), repeat=9)]
binary = np.array(binary)

@app.route('/', methods = ['GET', 'POST'])
def index():
    global filename
    if request.method == "POST":

        pedigree_selection = request.form.get('results-form')
        # print(pedigree_selection)

        ###############################################################################
        # EXPERIMENTING W/ CONVERTING STRING TO JSON... FAILED TODO() - INSPECT LATER #
        ###############################################################################

        # PEDIGREE 1'S DATA ATTRIBUTES
        ped1age = int(request.form.get("ped1Age"))
        ped1ldlc = int(request.form.get("ped1LDLChol"))
        ped1totc = int(request.form.get("ped1TOTChol"))
        ped1gender = request.form.get("ped1Gender")
        ped1cadstat = int(request.form.get("ped1CadStatus"))
        ped1cadage = int(request.form.get("ped1CadAge"))
        ped1tx = int(request.form.get("ped1TXStatus"))
        ped1dna = int(request.form.get("ped1DnaDxStatus"))
        ped1fhprob = request.form.get("ped1FhProb")


        # PEDIGREE 2'S DATA ATTRIBUTES
        ped2age = int(request.form.get("ped2Age"))
        ped2ldlc = int(request.form.get("ped2LDLChol"))
        ped2totc = int(request.form.get("ped2TOTChol"))
        ped2gender = request.form.get("ped2Gender")
        ped2cadstat = int(request.form.get("ped2CadStatus"))
        ped2cadage = int(request.form.get("ped2CadAge"))
        ped2tx = int(request.form.get("ped2TXStatus"))
        ped2dna = int(request.form.get("ped2DnaDxStatus"))
        ped2fhprob = request.form.get("ped2FhProb")

        # PEDIGREE 3'S DATA ATTRIBUTES
        ped3age = int(request.form.get("ped3Age"))
        ped3ldlc = int(request.form.get("ped3LDLChol"))
        ped3totc = int(request.form.get("ped3TOTChol"))
        ped3gender = request.form.get("ped3Gender")
        ped3cadstat = int(request.form.get("ped3CadStatus"))
        ped3cadage = int(request.form.get("ped3CadAge"))
        ped3tx = int(request.form.get("ped3TXStatus"))
        ped3dna = int(request.form.get("ped3DnaDxStatus"))
        ped3fhprob = request.form.get("ped3FhProb")

        # PEDIGREE 4'S DATA ATTRIBUTES
        ped4age = int(request.form.get("ped4Age"))
        ped4ldlc = int(request.form.get("ped4LDLChol"))
        ped4totc = int(request.form.get("ped4TOTChol"))
        ped4gender = request.form.get("ped4Gender")
        ped4cadstat = int(request.form.get("ped4CadStatus"))
        ped4cadage = int(request.form.get("ped4CadAge"))
        ped4tx = int(request.form.get("ped4TXStatus"))
        ped4dna = int(request.form.get("ped4DnaDxStatus"))
        ped4fhprob = request.form.get("ped4FhProb")

        # PEDIGREE 5'S DATA ATTRIBUTES
        ped5age = int(request.form.get("ped5Age"))
        ped5ldlc = int(request.form.get("ped5LDLChol"))
        ped5totc = int(request.form.get("ped5TOTChol"))
        ped5gender = request.form.get("ped5Gender")
        ped5cadstat = int(request.form.get("ped5CadStatus"))
        ped5cadage = int(request.form.get("ped5CadAge"))
        ped5tx = int(request.form.get("ped5TXStatus"))
        ped5dna = int(request.form.get("ped5DnaDxStatus"))
        ped5fhprob = request.form.get("ped5FhProb")

        # PEDIGREE 6'S DATA ATTRIBUTES
        ped6age = int(request.form.get("ped6Age"))
        ped6ldlc = int(request.form.get("ped6LDLChol"))
        ped6totc = int(request.form.get("ped6TOTChol"))
        ped6gender = request.form.get("ped6Gender")
        ped6cadstat = int(request.form.get("ped6CadStatus"))
        ped6cadage = int(request.form.get("ped6CadAge"))
        ped6tx = int(request.form.get("ped6TXStatus"))
        ped6dna = int(request.form.get("ped6DnaDxStatus"))
        ped6fhprob = request.form.get("ped6FhProb")

        # PEDIGREE 7'S DATA ATTRIBUTES
        ped7age = int(request.form.get("ped7Age"))
        ped7ldlc = int(request.form.get("ped7LDLChol"))
        ped7totc = int(request.form.get("ped7TOTChol"))
        ped7gender = request.form.get("ped7Gender")
        ped7cadstat = int(request.form.get("ped7CadStatus"))
        ped7cadage = int(request.form.get("ped7CadAge"))
        ped7tx = int(request.form.get("ped7TXStatus"))
        ped7dna = int(request.form.get("ped7DnaDxStatus"))
        ped7fhprob = request.form.get("ped7FhProb")

        # PEDIGREE 8'S DATA ATTRIBUTES
        ped8age = int(request.form.get("ped8Age"))
        ped8ldlc = int(request.form.get("ped8LDLChol"))
        ped8totc = int(request.form.get("ped8TOTChol"))
        ped8gender = request.form.get("ped8Gender")
        ped8cadstat = int(request.form.get("ped8CadStatus"))
        ped8cadage = int(request.form.get("ped8CadAge"))
        ped8tx = int(request.form.get("ped8TXStatus"))
        ped8dna = int(request.form.get("ped8DnaDxStatus"))
        ped8fhprob = request.form.get("ped8FhProb")

        # PEDIGREE 9'S DATA ATTRIBUTES
        ped9age = int(request.form.get("ped9Age"))
        ped9ldlc = int(request.form.get("ped9LDLChol"))
        ped9totc = int(request.form.get("ped9TOTChol"))
        ped9gender = request.form.get("ped9Gender")
        ped9cadstat = int(request.form.get("ped9CadStatus"))
        ped9cadage = int(request.form.get("ped9CadAge"))
        ped9tx = int(request.form.get("ped9TXStatus"))
        ped9dna = int(request.form.get("ped9DnaDxStatus"))
        ped9fhprob = request.form.get("ped9FhProb")

        pedFamFh = request.form.get("pedFamProb")

        ## ADDING ALL INPUT DATA TO A PANDAS DATAFRAME FOR PROCESSING
        pinput = pd.DataFrame(
            columns=["Age", "LDL-C", "TOT-C", "Gender", "Clinical-CAD", "CAD-Age", "TX-Status", "DNA-DX Status"]
            ,data=[ [ped1age, ped1ldlc, ped1totc, ped1gender, ped1cadstat, ped1cadage, ped1tx, ped1dna]
                , [ped2age, ped2ldlc, ped2totc, ped2gender, ped2cadstat, ped2cadage, ped2tx, ped2dna]
                , [ped3age, ped3ldlc, ped3totc, ped3gender, ped3cadstat, ped3cadage, ped3tx, ped3dna]
                , [ped4age, ped4ldlc, ped4totc, ped4gender, ped4cadstat, ped4cadage, ped4tx, ped4dna]
                , [ped5age, ped5ldlc, ped5totc, ped5gender, ped5cadstat, ped5cadage, ped5tx, ped5dna]
                , [ped6age, ped6ldlc, ped6totc, ped6gender, ped6cadstat, ped6cadage, ped6tx, ped6dna]
                , [ped7age, ped7ldlc, ped7totc, ped7gender, ped7cadstat, ped7cadage, ped7tx, ped7dna]
                , [ped8age, ped8ldlc, ped8totc, ped8gender, ped8cadstat, ped8cadage, ped8tx, ped8dna]
                , [ped9age, ped9ldlc, ped9totc, ped9gender, ped9cadstat, ped9cadage, ped9tx, ped9dna] ])

        dftoTable = pinput.copy()

        # CREATING ALL CALCULATIONS
        def ldlcfh(age, ldlc, totalc):
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
            if ldlc == 0 and totalc == 0:
                returnvar = 1
            else:
                if ldlc > 0:
                    if age < 20:
                        value1 = 1
                        meantrue = value1 * ldlcfhlessthan20mean
                        sdtrue = value1 * ldlcfhlessthan20sd
                        returnvar = stats.norm.pdf(ldlc, meantrue, sdtrue)
                        # print(returnvar)
                    elif 20 <= age < 30:
                        value1 = 1
                        meantrue = value1 * ldlcfh2030mean
                        sdtrue = value1 * ldlcfh2030sd
                        returnvar = stats.norm.pdf(ldlc, meantrue, sdtrue)
                        # print(returnvar)
                    elif age >= 30:
                        value1 = 1
                        meantrue = value1 * ldlcfh30plusmean
                        sdtrue = value1 * ldlcfh30plussd
                        returnvar = stats.norm.pdf(ldlc, meantrue, sdtrue)
                        # print(returnvar)
                    else:
                        returnvar = 1
                else:
                    if age < 20:
                        value1 = 1
                        meanfalse = value1 * totalcfhlessthan20mean
                        sdfalse = value1 * totalcfhlessthan20sd
                        returnvar = stats.norm.pdf(totalc, meanfalse, sdfalse)
                        # print(returnvar)
                    elif 20 <= age < 30:
                        value1 = 1
                        meanfalse = value1 * totalcfh2030mean
                        sdfalse = value1 * totalcfh2030sd
                        returnvar = stats.norm.pdf(totalc, meanfalse, sdfalse)
                        # print(returnvar)
                    elif age >= 30:
                        value1 = 1
                        meanfalse = value1 * totalcfh30plusmean
                        sdfalse = value1 * totalcfh30plussd
                        returnvar = stats.norm.pdf(totalc, meanfalse, sdfalse)
                        # print(returnvar)
                    else:
                        returnvar = 1
            return returnvar

        def ldlcnotfh(ldlc, age, totalc):
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
            if ldlc == 0 and totalc == 0:
                returnvar = 1
            else:
                if ldlc > 0:
                    if age < 20:
                        value1 = 1
                        meantrue = value1 * ldlcnotfhlessthan20mean
                        sdtrue = value1 * ldlcnotfhlessthan20sd
                        returnvar = stats.norm.pdf(ldlc, meantrue, sdtrue)
                        # print(returnvar)
                    elif 20 <= age < 30:
                        value1 = 1
                        meantrue = value1 * ldlcnotfh2030mean
                        sdtrue = value1 * ldlcnotfh2030sd
                        returnvar = stats.norm.pdf(ldlc, meantrue, sdtrue)
                        # print(returnvar)
                    elif age >= 30:
                        value1 = 1
                        meantrue = value1 * ldlcnotfh30plusmean
                        sdtrue = value1 * ldlcnotfh30plussd
                        returnvar = stats.norm.pdf(ldlc, meantrue, sdtrue)
                        # print(returnvar)
                    else:
                        returnvar = 1
                else:
                    if age < 20:
                        value1 = 1
                        meanfalse = value1 * totalcnotfhlessthan20mean
                        sdfalse = value1 * totalcnotfhlessthan20sd
                        returnvar = stats.norm.pdf(totalc, meanfalse, sdfalse)
                        # print(returnvar)
                    elif 20 <= age < 30:
                        value1 = 1
                        meanfalse = value1 * totalcnotfh2030mean
                        sdfalse = value1 * totalcnotfh2030sd
                        returnvar = stats.norm.pdf(totalc, meanfalse, sdfalse)
                        # print(returnvar)
                    elif age >= 30:
                        value1 = 1
                        meanfalse = value1 * totalcnotfh30plusmean
                        sdfalse = value1 * totalcnotfh30plussd
                        returnvar = stats.norm.pdf(totalc, meanfalse, sdfalse)
                        # print(returnvar)
                    else:
                        returnvar = 1
            return returnvar

        def TXPFISFH(ldlc, age, tx):
            calc = 0
            if tx == 9:
                calc = 1
                # print(calc)
            else:
                if ldlc > 100:
                    calc = tx * ((0.8205 * age - 1.8113) / 100) + (1 - tx) * (1 - (0.8205 * age - 1.8113) / 100)
                    # print(calc)
                else:
                    calc = tx * 1 + (1 - tx) * 1
                    # print(calc)
            return calc

        def TXPFISNOTFH(tx):
            calc = 0
            if tx == 9:
                calc = 1
                # print(calc)
            else:
                if tx == 1:
                    calc = 0.0001
                    # print(calc)
                else:
                    calc = 1 - 0.0001
                    # print(calc)
            return calc

        def CADPFISFH(clinicalCAD, gender, onsetAge, age):
            calc = 0
            if clinicalCAD == 9:
                calc = 1
                # print(calc, "Line 188")
            else:
                if gender == "m":
                    if clinicalCAD == 1:
                        calc = 0.832 / (1 + math.exp(0.124 * (52.9 - onsetAge)))
                        # print(calc, "Line 193")
                    else:
                        calc = 1 - (0.832 / (1 + math.exp(0.124 * (52.9 - age))))
                        # print(calc, "Line 196")
                else:
                    if clinicalCAD == 1:
                        calc = 0.601 / (1 + math.exp(0.155 * (54.7 - onsetAge)))
                        # print(calc, "Line 200")
                    else:
                        calc = 1 - (0.601 / (1 + math.exp(0.155 * (54.7 - age))))
                        # print(calc, "Line 203")
            return calc

        def CADISNOTFH(clinicalCAD, gender, onsetAge, age):
            calc = 0
            if clinicalCAD == 9:
                calc = 1
                # print(calc, " Line 210")
            else:
                if gender == "m":
                    if clinicalCAD == 1:
                        calc = 0.499 / (1 + math.exp(0.142 * (69.6 - onsetAge)))
                        # print(calc, " Line 215")
                    else:
                        calc = 1 - (0.499 / (1 + math.exp(0.142 * (69.6 - age))))
                        # print(calc, " Line 218")
                else:
                    if clinicalCAD == 1:
                        calc = 0.713 / (1 + math.exp(0.0981 * (88.6 - onsetAge)))
                        # print(calc, "Line 222")
                    else:
                        calc = 1 - (0.713 / (1 + math.exp(0.0981 * (88.6 - age))))
                        # print(calc, "Line 225")
            return calc

        # Calculating the Penetrance Functions
        def multiple():
            output = pd.DataFrame(
                columns=['ldlcfh1', 'ldlcnotfh1', 'txpfisfh1', 'txpfisnotfh1', 'cadpfisfh1', 'cadisnotfh1'])
            for i, j in pinput.iterrows():
                agei = j.values[0]
                ldlci = j.values[1]
                totalci = j.values[2]
                clincalcad = j.values[4]
                genderi = j.values[3]
                onsetage = j.values[5]
                txi = j.values[6]

                ldlcfh1 = ldlcfh(agei, ldlci, totalci)

                txpfisfh1 = TXPFISFH(ldlci, agei, txi)

                cadpfish1 = CADPFISFH(clincalcad, genderi, onsetage, agei)

                ldlcnotfh1 = ldlcnotfh(ldlci, agei, totalci)

                txpfisnotfh1 = TXPFISNOTFH(txi)

                cadisnotfh1 = CADISNOTFH(clincalcad, genderi, onsetage, agei)

                output.loc[i] = [ldlcfh1, ldlcnotfh1, txpfisfh1, txpfisnotfh1, cadpfish1, cadisnotfh1]

            return output

        # Creating calculation rows
        def FPP1():
            dna_dx1 = pinput.iloc[[0], [7]]
            fh_prob = 0.002
            trust = 0
            output = [trust]  # list that the function will return
            for item in binary:
                if dna_dx1.values == 1 and item[0] == 0:
                    right_side = 0
                    trust = (1 - fh_prob) * right_side
                    output.append(trust)
                    # print("Line 303 ", trust)
                else:
                    if item[0] > 0:
                        right_side = 1
                        trust = fh_prob * right_side
                        output.append(trust)  # append to the list instead of printing
                        # print("Line 308 ", trust)
                    else:
                        right_side = 1
                        trust = (1 - fh_prob) * right_side
                        output.append(trust)
                        # print("Line 312 ", trust)
            return output  # return list of values

        def FPP2():
            dna_dx2 = pinput.iloc[[1], [7]]
            fh_prob = 0.002
            trust = 0
            output = [trust]  # list that the function will return
            for item in binary:
                if dna_dx2.values == 1 and item[1] == 0:
                    right_side = 0
                    trust = (1 - fh_prob) * right_side
                    output.append(trust)
                    # print("Line 303 ", trust)
                else:
                    if item[1] > 0:
                        right_side = 1
                        trust = fh_prob * right_side
                        output.append(trust)  # append to the list instead of printing
                        # print("Line 308 ", trust)
                    else:
                        right_side = 1
                        trust = (1 - fh_prob) * right_side
                        output.append(trust)
                        # print("Line 312 ", trust)
            return output  # return list of values

        def FPP3():
            dna_dx3 = pinput.iloc[[2], [7]]
            fh_prob = 0.002
            trust = 0
            output = [trust]  # list that the function will return
            for item in binary:
                if dna_dx3.values == 1 and item[2] == 0:
                    right_side = 0
                    trust = (1 - fh_prob) * right_side
                    output.append(trust)
                    # print("Line 303 ", trust)
                else:
                    if item[2] > 0:
                        right_side = 1
                        trust = fh_prob * right_side
                        output.append(trust)  # append to the list instead of printing
                        # print("Line 308 ", trust)
                    else:
                        right_side = 1
                        trust = (1 - fh_prob) * right_side
                        output.append(trust)
                        # print("Line 312 ", trust)
            return output  # return list of values

        def TP4():
            transdna4 = pinput.iloc[[3], [7]]
            left_side = 0
            transprob4 = [left_side]
            for item in binary:
                if item[3] == 0 and transdna4.values == 1:
                    left_side = 0
                    transprob4.append(left_side)
                else:
                    if item[0] > 0 and item[1] > 0 and item[3] > 0:
                        multiply = 1
                        left_side = 0.75 * multiply
                        transprob4.append(left_side)
                    elif item[0] > 0 and item[1] > 0 and item[3] == 0:
                        multiply = 1
                        left_side = 0.25 * multiply
                        transprob4.append(left_side)
                    elif item[0] > 0 and item[1] == 0 and item[3] > 0:
                        multiply = 1
                        left_side = 0.5 * multiply
                        transprob4.append(left_side)
                    elif item[0] > 0 and item[1] == 0 and item[3] == 0:
                        multiply = 1
                        left_side = 0.5 * multiply
                        transprob4.append(left_side)
                    elif item[0] == 0 and item[1] > 0 and item[3] > 0:
                        multiply = 1
                        left_side = 0.5 * multiply
                        transprob4.append(left_side)
                    elif item[0] == 0 and item[1] > 0 and item[3] == 0:
                        multiply = 1
                        left_side = 0.5 * multiply
                        transprob4.append(left_side)
                    elif item[0] == 0 and item[1] == 0 and item[3] > 0:
                        multiply = 1
                        left_side = 0 * multiply
                        transprob4.append(left_side)
                    elif item[0] == 0 and item[1] == 0 and item[3] == 0:
                        multiply = 1
                        left_side = 1 * multiply
                        transprob4.append(left_side)
            return transprob4

        def TP5():
            transdna5 = pinput.iloc[[4], [7]]
            multiply = 1
            left_side = 0
            transprob5 = [left_side]
            for item in binary:
                if item[4] == 0 and transdna5.values == 1:
                    left_side = 0
                    transprob5.append(left_side)
                else:
                    if item[0] > 0 and item[1] > 0 and item[4] > 0:
                        left_side = 0.75 * multiply
                        transprob5.append(left_side)
                    elif item[0] > 0 and item[1] > 0 and item[4] == 0:
                        left_side = 0.25 * multiply
                        transprob5.append(left_side)
                    elif item[0] > 0 and item[1] == 0 and item[4] > 0:
                        left_side = 0.5 * multiply
                        transprob5.append(left_side)
                    elif item[0] > 0 and item[1] == 0 and item[4] == 0:
                        left_side = 0.5 * multiply
                        transprob5.append(left_side)
                    elif item[0] == 0 and item[1] > 0 and item[4] > 0:
                        left_side = 0.5 * multiply
                        transprob5.append(left_side)
                    elif item[0] == 0 and item[1] > 0 and item[4] == 0:
                        left_side = 0.5 * multiply
                        transprob5.append(left_side)
                    elif item[0] == 0 and item[1] == 0 and item[4] > 0:
                        left_side = 0 * multiply
                        transprob5.append(left_side)
                    elif item[0] == 0 and item[1] == 0 and item[4] == 0:
                        left_side = 1 * multiply
                        transprob5.append(left_side)
            return transprob5

        def TP6():
            transdna6 = pinput.iloc[[5], [7]]
            multiply = 1
            left_side = 0
            transprob6 = [left_side]
            for item in binary:
                if item[5] == 0 and transdna6.values == 1:
                    left_side = 0
                    transprob6.append(left_side)
                else:
                    if item[0] > 0 and item[1] > 0 and item[5] > 0:
                        left_side = 0.75 * multiply
                        transprob6.append(left_side)
                    elif item[0] > 0 and item[1] > 0 and item[5] == 0:
                        left_side = 0.25 * multiply
                        transprob6.append(left_side)
                    elif item[0] > 0 and item[1] == 0 and item[5] > 0:
                        left_side = 0.5 * multiply
                        transprob6.append(left_side)
                    elif item[0] > 0 and item[1] == 0 and item[5] == 0:
                        left_side = 0.5 * multiply
                        transprob6.append(left_side)
                    elif item[0] == 0 and item[1] > 0 and item[5] > 0:
                        left_side = 0.5 * multiply
                        transprob6.append(left_side)
                    elif item[0] == 0 and item[1] > 0 and item[5] == 0:
                        left_side = 0.5 * multiply
                        transprob6.append(left_side)
                    elif item[0] == 0 and item[1] == 0 and item[5] > 0:
                        left_side = 0 * multiply
                        transprob6.append(left_side)
                    elif item[0] == 0 and item[1] == 0 and item[5] == 0:
                        left_side = 1 * multiply
                        transprob6.append(left_side)
            return transprob6

        def TP7():
            transdna7 = pinput.iloc[[6], [7]]
            multiply = 1
            left_side = 0
            transprob7 = [left_side]
            for item in binary:
                if item[6] == 0 and transdna7.values == 1:
                    left_side = 0
                    transprob7.append(left_side)
                else:
                    if item[2] > 0 and item[5] > 0 and item[6] > 0:
                        left_side = 0.75 * multiply
                        transprob7.append(left_side)
                    elif item[2] > 0 and item[5] > 0 and item[6] == 0:
                        left_side = 0.25 * multiply
                        transprob7.append(left_side)
                    elif item[2] > 0 and item[5] == 0 and item[6] > 0:
                        left_side = 0.5 * multiply
                        transprob7.append(left_side)
                    elif item[2] > 0 and item[5] == 0 and item[6] == 0:
                        left_side = 0.5 * multiply
                        transprob7.append(left_side)
                    elif item[2] == 0 and item[5] > 0 and item[6] > 0:
                        left_side = 0.5 * multiply
                        transprob7.append(left_side)
                    elif item[2] == 0 and item[5] > 0 and item[6] == 0:
                        left_side = 0.5 * multiply
                        transprob7.append(left_side)
                    elif item[2] == 0 and item[5] == 0 and item[6] > 0:
                        left_side = 0 * multiply
                        transprob7.append(left_side)
                    elif item[2] == 0 and item[5] == 0 and item[6] == 0:
                        left_side = 1 * multiply
                        transprob7.append(left_side)

            return transprob7

        def TP8():
            transdna8 = pinput.iloc[[7], [7]]
            multiply = 1
            left_side = 0
            transprob8 = [left_side]
            for item in binary:
                if item[7] == 0 and transdna8.values == 1:
                    left_side = 0
                    transprob8.append(left_side)
                else:
                    if item[2] > 0 and item[5] > 0 and item[7] > 0:
                        left_side = 0.75 * multiply
                        transprob8.append(left_side)
                    elif item[2] > 0 and item[5] > 0 and item[7] == 0:
                        left_side = 0.25 * multiply
                        transprob8.append(left_side)
                    elif item[2] > 0 and item[5] == 0 and item[7] > 0:
                        left_side = 0.5 * multiply
                        transprob8.append(left_side)
                    elif item[2] > 0 and item[5] == 0 and item[7] == 0:
                        left_side = 0.5 * multiply
                        transprob8.append(left_side)
                    elif item[2] == 0 and item[5] > 0 and item[7] > 0:
                        left_side = 0.5 * multiply
                        transprob8.append(left_side)
                    elif item[2] == 0 and item[5] > 0 and item[7] == 0:
                        left_side = 0.5 * multiply
                        transprob8.append(left_side)
                    elif item[2] == 0 and item[5] == 0 and item[7] > 0:
                        left_side = 0 * multiply
                        transprob8.append(left_side)
                    elif item[2] == 0 and item[5] == 0 and item[7] == 0:
                        left_side = 1 * multiply
                        transprob8.append(left_side)

            return transprob8

        def TP9():
            transdna9 = pinput.iloc[[8], [7]]
            multiply = 1
            left_side = 0
            transprob9 = [left_side]
            for item in binary:
                if item[8] == 0 and transdna9.values == 1:
                    left_side = 0
                    transprob9.append(left_side)
                else:
                    if item[2] > 0 and item[5] > 0 and item[8] > 0:
                        left_side = 0.75 * multiply
                        transprob9.append(left_side)
                    elif item[2] > 0 and item[5] > 0 and item[8] == 0:
                        left_side = 0.25 * multiply
                        transprob9.append(left_side)
                    elif item[2] > 0 and item[5] == 0 and item[8] > 0:
                        left_side = 0.5 * multiply
                        transprob9.append(left_side)
                    elif item[2] > 0 and item[5] == 0 and item[8] == 0:
                        left_side = 0.5 * multiply
                        transprob9.append(left_side)
                    elif item[2] == 0 and item[5] > 0 and item[8] > 0:
                        left_side = 0.5 * multiply
                        transprob9.append(left_side)
                    elif item[2] == 0 and item[5] > 0 and item[8] == 0:
                        left_side = 0.5 * multiply
                        transprob9.append(left_side)
                    elif item[2] == 0 and item[5] == 0 and item[8] > 0:
                        left_side = 0 * multiply
                        transprob9.append(left_side)
                    elif item[2] == 0 and item[5] == 0 and item[8] == 0:
                        left_side = 1 * multiply
                        transprob9.append(left_side)

            return transprob9

        def LDLC1():
            ldlcage1 = pinput.iloc[0, 0]
            ldlccheck1 = pinput.iloc[0, 1]
            ldlctotalc1 = pinput.iloc[0, 2]
            isfh = ldlcfh(ldlcage1, ldlccheck1, ldlctotalc1)
            notfh = ldlcnotfh(ldlccheck1, ldlcage1, ldlctotalc1)
            ldlcprob = 0
            ldlcoutput = [ldlcprob]
            for item in binary:
                if item[0] == 0:
                    ldlcprob = notfh
                    ldlcoutput.append(ldlcprob)
                else:
                    ldlcprob = isfh
                    ldlcoutput.append(ldlcprob)
            return ldlcoutput

        def LDLC2():
            ldlcage2 = pinput.iloc[1, 0]
            ldlccheck2 = pinput.iloc[1, 1]
            ldlctotalc2 = pinput.iloc[1, 2]
            isfh = ldlcfh(ldlcage2, ldlccheck2, ldlctotalc2)
            notfh = ldlcnotfh(ldlccheck2, ldlcage2, ldlctotalc2)
            ldlcprob = 0
            ldlcoutput = [ldlcprob]
            for item in binary:
                if item[1] == 0:
                    ldlcprob = notfh
                    ldlcoutput.append(ldlcprob)
                else:
                    ldlcprob = isfh
                    ldlcoutput.append(ldlcprob)
            return ldlcoutput

        def LDLC3():
            ldlcage3 = pinput.iloc[2, 0]
            ldlccheck3 = pinput.iloc[2, 1]
            ldlctotalc3 = pinput.iloc[2, 2]
            isfh = ldlcfh(ldlcage3, ldlccheck3, ldlctotalc3)
            notfh = ldlcnotfh(ldlccheck3, ldlcage3, ldlctotalc3)
            ldlcprob = 0
            ldlcoutput = [ldlcprob]
            for item in binary:
                if item[2] == 0:
                    ldlcprob = notfh
                    ldlcoutput.append(ldlcprob)
                else:
                    ldlcprob = isfh
                    ldlcoutput.append(ldlcprob)
            return ldlcoutput

        def LDLC4():
            ldlcage4 = pinput.iloc[3, 0]
            ldlccheck4 = pinput.iloc[3, 1]
            ldlctotalc4 = pinput.iloc[3, 2]
            isfh = ldlcfh(ldlcage4, ldlccheck4, ldlctotalc4)
            notfh = ldlcnotfh(ldlccheck4, ldlcage4, ldlctotalc4)
            ldlcprob = 0
            ldlcoutput = [ldlcprob]
            for item in binary:
                if item[3] == 0:
                    ldlcprob = notfh
                    ldlcoutput.append(ldlcprob)
                else:
                    ldlcprob = isfh
                    ldlcoutput.append(ldlcprob)
            return ldlcoutput

        def LDLC5():
            ldlcage5 = pinput.iloc[4, 0]
            ldlccheck5 = pinput.iloc[4, 1]
            ldlctotalc5 = pinput.iloc[4, 2]
            isfh = ldlcfh(ldlcage5, ldlccheck5, ldlctotalc5)
            notfh = ldlcnotfh(ldlccheck5, ldlcage5, ldlctotalc5)
            ldlcprob = 0
            ldlcoutput = [ldlcprob]
            for item in binary:
                if item[4] == 0:
                    ldlcprob = notfh
                    ldlcoutput.append(ldlcprob)
                else:
                    ldlcprob = isfh
                    ldlcoutput.append(ldlcprob)
            return ldlcoutput

        def LDLC6():
            ldlcage6 = pinput.iloc[5, 0]
            ldlccheck6 = pinput.iloc[5, 1]
            ldlctotalc6 = pinput.iloc[5, 2]
            isfh = ldlcfh(ldlcage6, ldlccheck6, ldlctotalc6)
            notfh = ldlcnotfh(ldlccheck6, ldlcage6, ldlctotalc6)
            ldlcprob = 0
            ldlcoutput = [ldlcprob]
            for item in binary:
                if item[5] == 0:
                    ldlcprob = notfh
                    ldlcoutput.append(ldlcprob)
                else:
                    ldlcprob = isfh
                    ldlcoutput.append(ldlcprob)
            return ldlcoutput

        def LDLC7():
            ldlcage7 = pinput.iloc[6, 0]
            ldlccheck7 = pinput.iloc[6, 1]
            ldlctotalc7 = pinput.iloc[6, 2]
            isfh = ldlcfh(ldlcage7, ldlccheck7, ldlctotalc7)
            notfh = ldlcnotfh(ldlccheck7, ldlcage7, ldlctotalc7)
            ldlcprob = 0
            ldlcoutput = [ldlcprob]
            for item in binary:
                if item[6] == 0:
                    ldlcprob = notfh
                    ldlcoutput.append(ldlcprob)
                else:
                    ldlcprob = isfh
                    ldlcoutput.append(ldlcprob)
            return ldlcoutput

        def LDLC8():
            ldlcage8 = pinput.iloc[7, 0]
            ldlccheck8 = pinput.iloc[7, 1]
            ldlctotalc8 = pinput.iloc[7, 2]
            isfh = ldlcfh(ldlcage8, ldlccheck8, ldlctotalc8)
            notfh = ldlcnotfh(ldlccheck8, ldlcage8, ldlctotalc8)
            ldlcprob = 0
            ldlcoutput = [ldlcprob]
            for item in binary:
                if item[7] == 0:
                    ldlcprob = notfh
                    ldlcoutput.append(ldlcprob)
                else:
                    ldlcprob = isfh
                    ldlcoutput.append(ldlcprob)
            return ldlcoutput

        def LDLC9():
            ldlcage9 = pinput.iloc[8, 0]
            ldlccheck9 = pinput.iloc[8, 1]
            ldlctotalc9 = pinput.iloc[8, 2]
            isfh = ldlcfh(ldlcage9, ldlccheck9, ldlctotalc9)
            notfh = ldlcnotfh(ldlccheck9, ldlcage9, ldlctotalc9)
            ldlcprob = 0
            ldlcoutput = [ldlcprob]
            for item in binary:
                if item[8] == 0:
                    ldlcprob = notfh
                    ldlcoutput.append(ldlcprob)
                else:
                    ldlcprob = isfh
                    ldlcoutput.append(ldlcprob)
            return ldlcoutput

        def TX1():
            tx1 = pinput.iloc[0, 6]
            txldlc1 = pinput.iloc[0, 1]
            txage1 = pinput.iloc[0, 0]
            istx = TXPFISFH(txldlc1, txage1, tx1)
            nottx = TXPFISNOTFH(tx1)
            txprob = 0
            txoutput = [txprob]
            for item in binary:
                if item[0] == 1:
                    txprob = istx
                    txoutput.append(txprob)
                else:
                    txprob = nottx
                    txoutput.append(txprob)
            return txoutput

        def TX2():
            tx2 = pinput.iloc[1, 6]
            txldlc2 = pinput.iloc[1, 1]
            txage2 = pinput.iloc[1, 0]
            istx = TXPFISFH(txldlc2, txage2, tx2)
            nottx = TXPFISNOTFH(tx2)
            txprob = 0
            txoutput = [txprob]
            for item in binary:
                if item[1] == 1:
                    txprob = istx
                    txoutput.append(txprob)
                else:
                    txprob = nottx
                    txoutput.append(txprob)
            return txoutput

        def TX3():
            tx3 = pinput.iloc[2, 6]
            txldlc3 = pinput.iloc[2, 1]
            txage3 = pinput.iloc[2, 0]
            istx = TXPFISFH(txldlc3, txage3, tx3)
            nottx = TXPFISNOTFH(tx3)
            txprob = 0
            txoutput = [txprob]
            for item in binary:
                if item[2] == 1:
                    txprob = istx
                    txoutput.append(txprob)
                else:
                    txprob = nottx
                    txoutput.append(txprob)
            return txoutput

        def TX4():
            tx4 = pinput.iloc[3, 6]
            txldlc4 = pinput.iloc[3, 1]
            txage4 = pinput.iloc[3, 0]
            istx = TXPFISFH(txldlc4, txage4, tx4)
            nottx = TXPFISNOTFH(tx4)
            txprob = 0
            txoutput = [txprob]
            for item in binary:
                if item[3] == 1:
                    txprob = istx
                    txoutput.append(txprob)
                else:
                    txprob = nottx
                    txoutput.append(txprob)
            return txoutput

        def TX5():
            tx5 = pinput.iloc[4, 6]
            txldlc5 = pinput.iloc[4, 1]
            txage5 = pinput.iloc[4, 0]
            istx = TXPFISFH(txldlc5, txage5, tx5)
            nottx = TXPFISNOTFH(tx5)
            txprob = 0
            txoutput = [txprob]
            for item in binary:
                if item[4] == 1:
                    txprob = istx
                    txoutput.append(txprob)
                else:
                    txprob = nottx
                    txoutput.append(txprob)
            return txoutput

        def TX6():
            tx6 = pinput.iloc[5, 6]
            txldlc6 = pinput.iloc[5, 1]
            txage6 = pinput.iloc[5, 0]
            istx = TXPFISFH(txldlc6, txage6, tx6)
            nottx = TXPFISNOTFH(tx6)
            txprob = 0
            txoutput = [txprob]
            for item in binary:
                if item[5] == 1:
                    txprob = istx
                    txoutput.append(txprob)
                else:
                    txprob = nottx
                    txoutput.append(txprob)
            return txoutput

        def TX7():
            tx7 = pinput.iloc[6, 6]
            txldlc7 = pinput.iloc[6, 1]
            txage7 = pinput.iloc[6, 0]
            istx = TXPFISFH(txldlc7, txage7, tx7)
            nottx = TXPFISNOTFH(tx7)
            txprob = 0
            txoutput = [txprob]
            for item in binary:
                if item[6] == 1:
                    txprob = istx
                    txoutput.append(txprob)
                else:
                    txprob = nottx
                    txoutput.append(txprob)
            return txoutput

        def TX8():
            tx8 = pinput.iloc[7, 6]
            txldlc8 = pinput.iloc[7, 1]
            txage8 = pinput.iloc[7, 0]
            istx = TXPFISFH(txldlc8, txage8, tx8)
            nottx = TXPFISNOTFH(tx8)
            txprob = 0
            txoutput = [txprob]
            for item in binary:
                if item[7] == 1:
                    txprob = istx
                    txoutput.append(txprob)
                else:
                    txprob = nottx
                    txoutput.append(txprob)
            return txoutput

        def TX9():
            tx9 = pinput.iloc[8, 6]
            txldlc9 = pinput.iloc[8, 1]
            txage9 = pinput.iloc[8, 0]
            istx = TXPFISFH(txldlc9, txage9, tx9)
            nottx = TXPFISNOTFH(tx9)
            txprob = 0
            txoutput = [txprob]
            for item in binary:
                if item[8] == 1:
                    txprob = istx
                    txoutput.append(txprob)
                else:
                    txprob = nottx
                    txoutput.append(txprob)
            return txoutput

        def CAD1():
            cadclinical1 = pinput.iloc[0, 4]
            cadgender1 = pinput.iloc[0, 3]
            cadonsetage1 = pinput.iloc[0, 5]
            cadage1 = pinput.iloc[0, 0]
            iscad1 = CADPFISFH(cadclinical1, cadgender1, cadonsetage1, cadage1)
            isnotcad1 = CADISNOTFH(cadclinical1, cadgender1, cadonsetage1, cadage1)
            cadprob = 0
            cadoutput = [cadprob]
            for item in binary:
                if item[0] == 1:
                    cadprob = iscad1
                    cadoutput.append(cadprob)
                else:
                    cadprob = isnotcad1
                    cadoutput.append(cadprob)
            return cadoutput

        def CAD2():
            cadclinical2 = pinput.iloc[1, 4]
            cadgender2 = pinput.iloc[1, 3]
            cadonsetage2 = pinput.iloc[1, 5]
            cadage2 = pinput.iloc[1, 0]
            iscad2 = CADPFISFH(cadclinical2, cadgender2, cadonsetage2, cadage2)
            isnotcad2 = CADISNOTFH(cadclinical2, cadgender2, cadonsetage2, cadage2)
            cadprob = 0
            cadoutput = [cadprob]
            for item in binary:
                if item[1] == 1:
                    cadprob = iscad2
                    cadoutput.append(cadprob)
                else:
                    cadprob = isnotcad2
                    cadoutput.append(cadprob)
            return cadoutput

        def CAD3():
            cadclinical3 = pinput.iloc[2, 4]
            cadgender3 = pinput.iloc[2, 3]
            cadonsetage3 = pinput.iloc[2, 5]
            cadage3 = pinput.iloc[2, 0]
            iscad3 = CADPFISFH(cadclinical3, cadgender3, cadonsetage3, cadage3)
            isnotcad3 = CADISNOTFH(cadclinical3, cadgender3, cadonsetage3, cadage3)
            cadprob = 0
            cadoutput = [cadprob]
            for item in binary:
                if item[2] == 1:
                    cadprob = iscad3
                    cadoutput.append(cadprob)
                else:
                    cadprob = isnotcad3
                    cadoutput.append(cadprob)
            return cadoutput

        def CAD4():
            cadclinical4 = pinput.iloc[3, 4]
            cadgender4 = pinput.iloc[3, 3]
            cadonsetage4 = pinput.iloc[3, 5]
            cadage4 = pinput.iloc[3, 0]
            iscad4 = CADPFISFH(cadclinical4, cadgender4, cadonsetage4, cadage4)
            isnotcad4 = CADISNOTFH(cadclinical4, cadgender4, cadonsetage4, cadage4)
            cadprob = 0
            cadoutput = [cadprob]
            for item in binary:
                if item[3] == 1:
                    cadprob = iscad4
                    cadoutput.append(cadprob)
                else:
                    cadprob = isnotcad4
                    cadoutput.append(cadprob)
            return cadoutput

        def CAD5():
            cadclinical5 = pinput.iloc[4, 4]
            cadgender5 = pinput.iloc[4, 3]
            cadonsetage5 = pinput.iloc[4, 5]
            cadage5 = pinput.iloc[4, 0]
            iscad5 = CADPFISFH(cadclinical5, cadgender5, cadonsetage5, cadage5)
            isnotcad5 = CADISNOTFH(cadclinical5, cadgender5, cadonsetage5, cadage5)
            cadprob = 0
            cadoutput = [cadprob]
            for item in binary:
                if item[4] == 1:
                    cadprob = iscad5
                    cadoutput.append(cadprob)
                else:
                    cadprob = isnotcad5
                    cadoutput.append(cadprob)
            return cadoutput

        def CAD6():
            cadclinical6 = pinput.iloc[5, 4]
            cadgender6 = pinput.iloc[5, 3]
            cadonsetage6 = pinput.iloc[5, 5]
            cadage6 = pinput.iloc[5, 0]
            iscad6 = CADPFISFH(cadclinical6, cadgender6, cadonsetage6, cadage6)
            isnotcad6 = CADISNOTFH(cadclinical6, cadgender6, cadonsetage6, cadage6)
            cadprob = 0
            cadoutput = [cadprob]
            for item in binary:
                if item[5] == 1:
                    cadprob = iscad6
                    cadoutput.append(cadprob)
                else:
                    cadprob = isnotcad6
                    cadoutput.append(cadprob)
            return cadoutput

        def CAD7():
            cadclinical7 = pinput.iloc[6, 4]
            cadgender7 = pinput.iloc[6, 3]
            cadonsetage7 = pinput.iloc[6, 5]
            cadage7 = pinput.iloc[6, 0]
            iscad7 = CADPFISFH(cadclinical7, cadgender7, cadonsetage7, cadage7)
            isnotcad7 = CADISNOTFH(cadclinical7, cadgender7, cadonsetage7, cadage7)
            cadprob = 0
            cadoutput = [cadprob]
            for item in binary:
                if item[6] == 1:
                    cadprob = iscad7
                    cadoutput.append(cadprob)
                else:
                    cadprob = isnotcad7
                    cadoutput.append(cadprob)
            return cadoutput

        def CAD8():
            cadclinical8 = pinput.iloc[7, 4]
            cadgender8 = pinput.iloc[7, 3]
            cadonsetage8 = pinput.iloc[7, 5]
            cadage8 = pinput.iloc[7, 0]
            iscad8 = CADPFISFH(cadclinical8, cadgender8, cadonsetage8, cadage8)
            isnotcad8 = CADISNOTFH(cadclinical8, cadgender8, cadonsetage8, cadage8)
            cadprob = 0
            cadoutput = [cadprob]
            for item in binary:
                if item[7] == 1:
                    cadprob = iscad8
                    cadoutput.append(cadprob)
                else:
                    cadprob = isnotcad8
                    cadoutput.append(cadprob)
            return cadoutput

        def CAD9():
            cadclinical9 = pinput.iloc[8, 4]
            cadgender9 = pinput.iloc[8, 3]
            cadonsetage9 = pinput.iloc[8, 5]
            cadage9 = pinput.iloc[8, 0]
            iscad9 = CADPFISFH(cadclinical9, cadgender9, cadonsetage9, cadage9)
            isnotcad9 = CADISNOTFH(cadclinical9, cadgender9, cadonsetage9, cadage9)
            cadprob = 0
            cadoutput = [cadprob]
            for item in binary:
                if item[8] == 1:
                    cadprob = iscad9
                    cadoutput.append(cadprob)
                else:
                    cadprob = isnotcad9
                    cadoutput.append(cadprob)
            return cadoutput

        # Calculating Family Probability
        def family():
            value = 0
            output = [value]
            for row in binary:
                if row.any() == 1:
                    value = 1
                    output.append(value)
                elif row.any() == 0:
                    value = 0
                    output.append(value)
            return output

        # Calculating person likelihood
        def person1():
            value = 0
            output = [value]
            for item in binary:
                if item[0] == 1:
                    value = 1
                    output.append(value)
                else:
                    value = 0
                    output.append(value)
            return output

        def person2():
            value = 0
            output = [value]
            for item in binary:
                if item[1] == 1:
                    value = 1
                    output.append(value)
                else:
                    value = 0
                    output.append(value)
            return output

        def person3():
            value = 0
            output = [value]
            for item in binary:
                if item[2] == 1:
                    value = 1
                    output.append(value)
                else:
                    value = 0
                    output.append(value)
            return output

        def person4():
            value = 0
            output = [value]
            for item in binary:
                if item[3] == 1:
                    value = 1
                    output.append(value)
                else:
                    value = 0
                    output.append(value)
            return output

        def person5():
            value = 0
            output = [value]
            for item in binary:
                if item[4] == 1:
                    value = 1
                    output.append(value)
                else:
                    value = 0
                    output.append(value)
            return output

        def person6():
            value = 0
            output = [value]
            for item in binary:
                if item[5] == 1:
                    value = 1
                    output.append(value)
                else:
                    value = 0
                    output.append(value)
            return output

        def person7():
            value = 0
            output = [value]
            for item in binary:
                if item[6] == 1:
                    value = 1
                    output.append(value)
                else:
                    value = 0
                    output.append(value)
            return output

        def person8():
            value = 0
            output = [value]
            for item in binary:
                if item[7] == 1:
                    value = 1
                    output.append(value)
                else:
                    value = 0
                    output.append(value)
            return output

        def person9():
            value = 0
            output = [value]
            for item in binary:
                if item[8] == 1:
                    value = 1
                    output.append(value)
                else:
                    value = 0
                    output.append(value)
            return output

        def stringlikestuff():
            founder = pd.DataFrame( [FPP1(), FPP2(), FPP3()] ).transpose()
            founderprob = founder.iloc[1:, :]

            transmission = pd.DataFrame( [TP4(), TP5(), TP6(), TP7(), TP8(), TP9()] ).transpose()
            transmissionprob = transmission.iloc[1:, :]
            ldldf = pd.DataFrame( [LDLC1(), LDLC2(), LDLC3(), LDLC4(), LDLC5(), LDLC6(), LDLC7(), LDLC8(), LDLC9()]
                                  ).transpose()
            ldlarray = ldldf.iloc[1:, :]

            txdf = pd.DataFrame( [TX1(), TX2(), TX3(), TX4(), TX5(), TX6(), TX7(), TX8(), TX9()] ).transpose()
            txarray = txdf.iloc[1:, :]

            caddf = pd.DataFrame( [CAD1(), CAD2(), CAD3(), CAD4(), CAD5(), CAD6(), CAD7(), CAD8(), CAD9()] ).transpose()
            cadarray = caddf.iloc[1:, :]

            # Creating the table by Calculating the String Probabilites
            probs = pd.DataFrame([
                FPP1(), FPP2(), FPP3(), TP4(), TP5(), TP6(), TP7(), TP8(), TP9()
                , LDLC1(), LDLC2(), LDLC3(), LDLC4(), LDLC5(), LDLC6(), LDLC7(), LDLC8(), LDLC9()
                , TX1(), TX2(), TX3(), TX4(), TX5(), TX6(), TX7(), TX8(), TX9()
                , CAD1(), CAD2(), CAD3(), CAD4(), CAD5(), CAD6(), CAD7(), CAD8(), CAD9()
            ]).transpose()

            # Creating 4 sections
            section1 = pd.DataFrame( [FPP1(), FPP2(), FPP3(), TP4(), TP5(), TP6(), TP7(), TP8(), TP9()]
                                     ).transpose()
            section2 = pd.DataFrame( [LDLC1(), LDLC2(), LDLC3(), LDLC4(), LDLC5(), LDLC6(), LDLC7(), LDLC8(), LDLC9()]
                                     ).transpose()
            section3 = pd.DataFrame( [TX1(), TX2(), TX3(), TX4(), TX5(), TX6(), TX7(), TX8(), TX9()]
                                     ).transpose()
            section4 = pd.DataFrame( [CAD1(), CAD2(), CAD3(), CAD4(), CAD5(), CAD6(), CAD7(), CAD8(), CAD9()]
                                     ).transpose()
            section1prod = section1.prod(axis=1)
            section2prod = section2.prod(axis=1)
            section3prod = section3.prod(axis=1)
            section4prod = section4.prod(axis=1)

            # Creating 1 dataframe with the products of 4 sections
            ultimateprod = pd.DataFrame([ section1prod, section2prod, section3prod, section4prod ]).transpose()
            probs["String Likelihood"] = ultimateprod.prod(axis=1)
            string = probs.iloc[1:, :]
            stringlike = pd.DataFrame([ string[ "String Likelihood" ] ]).transpose()

            return stringlike

        def stringsumstuff():
            probs = pd.DataFrame(
                [FPP1(), FPP2(), FPP3(), TP4(), TP5(), TP6(), TP7(), TP8(), TP9(), LDLC1(), LDLC2(), LDLC3(), LDLC4(),
                 LDLC5(), LDLC6(), LDLC7(),
                 LDLC8(), LDLC9(), TX1(), TX2(), TX3(), TX4(), TX5(), TX6(), TX7(), TX8(), TX9(), CAD1(), CAD2(),
                 CAD3(), CAD4(), CAD5(), CAD6(),
                 CAD7(), CAD8(), CAD9()]).transpose()
            # Creating 4 sections
            section1 = pd.DataFrame( [FPP1(), FPP2(), FPP3(), TP4(), TP5(), TP6(), TP7(), TP8(), TP9() ]
                                     ).transpose()
            section2 = pd.DataFrame( [LDLC1(), LDLC2(), LDLC3(), LDLC4(), LDLC5(), LDLC6(), LDLC7(), LDLC8(), LDLC9() ]
                                     ).transpose()
            section3 = pd.DataFrame( [TX1(), TX2(), TX3(), TX4(), TX5(), TX6(), TX7(), TX8(), TX9()]
                                     ).transpose()
            section4 = pd.DataFrame( [CAD1(), CAD2(), CAD3(), CAD4(), CAD5(), CAD6(), CAD7(), CAD8(), CAD9() ]
                                     ).transpose()
            # Cut off the first row
            # Creating products of 4 sections
            section1prod = section1.prod(axis=1)
            section2prod = section2.prod(axis=1)
            section3prod = section3.prod(axis=1)
            section4prod = section4.prod(axis=1)

            # Creating 1 dataframe with the products of 4 sections
            ultimateprod = pd.DataFrame( [section1prod, section2prod, section3prod, section4prod] ).transpose()
            probs["String Likelihood"] = ultimateprod.prod(axis=1)
            string = probs.iloc[1:, :]
            stringsum = pd.DataFrame( [string["String Likelihood"].sum()] )
            return stringsum

        def famsumstuff():
            stringlike = stringlikestuff()
            fam1 = pd.DataFrame([ family() ]).transpose()
            fam = fam1.iloc[1:, :]
            familylikelihood = fam.mul(stringlike.values)
            familylikelihood.columns = ["Family Likelihood"]
            famsum = pd.DataFrame([ familylikelihood[ "Family Likelihood" ].sum() ])

            return famsum

        def person1stuff():
            stringlike = stringlikestuff()
            person1f = pd.DataFrame([ person1() ]).transpose()
            person1df = person1f.iloc[1:, :]
            person1likely = person1df.mul(stringlike.values)
            person1likely.columns = ["Person 1 Likelihood"]
            person1sum = pd.DataFrame([ person1likely[ "Person 1 Likelihood" ].sum() ])

            return person1sum

        def person2stuff():
            stringlike = stringlikestuff()
            person2f = pd.DataFrame([ person2() ]).transpose()
            person2df = person2f.iloc[1:, :]
            person2likely = person2df.mul(stringlike.values)
            person2likely.columns = ["Person 2 Likelihood"]
            person2sum = pd.DataFrame([ person2likely[ "Person 2 Likelihood" ].sum() ])

            return person2sum

        def person3stuff():
            stringlike = stringlikestuff()
            person3f = pd.DataFrame([ person3() ]).transpose()
            person3df = person3f.iloc[1:, :]
            person3likely = person3df.mul(stringlike.values)
            person3likely.columns = ["Person 3 Likelihood"]
            person3sum = pd.DataFrame([ person3likely[ "Person 3 Likelihood" ].sum() ])

            return person3sum

        def person4stuff():
            stringlike = stringlikestuff()
            person4f = pd.DataFrame([ person4() ]).transpose()
            person4df = person4f.iloc[1:, :]
            person4likely = person4df.mul(stringlike.values)
            person4likely.columns = ["Person 4 Likelihood"]
            person4sum = pd.DataFrame([ person4likely["Person 4 Likelihood"].sum() ])

            return person4sum

        def person5stuff():
            stringlike = stringlikestuff()
            person5f = pd.DataFrame([ person5() ]).transpose()
            person5df = person5f.iloc[1:, :]
            person5likely = person5df.mul(stringlike.values)
            person5likely.columns = ["Person 5 Likelihood"]
            person5sum = pd.DataFrame([ person5likely[ "Person 5 Likelihood" ].sum() ])

            return person5sum

        def person6stuff():
            stringlike = stringlikestuff()
            person6f = pd.DataFrame([ person6() ]).transpose()
            person6df = person6f.iloc[1:, :]
            person6likely = person6df.mul(stringlike.values)
            person6likely.columns = ["Person 6 Likelihood"]
            person6sum = pd.DataFrame([ person6likely["Person 6 Likelihood"].sum() ])

            return person6sum

        def person7stuff():
            stringlike = stringlikestuff()
            person7f = pd.DataFrame([ person7() ]).transpose()
            person7df = person7f.iloc[1:, :]
            person7likely = person7df.mul(stringlike.values)
            person7likely.columns = ["Person 7 Likelihood"]
            person7sum = pd.DataFrame([ person7likely[ "Person 7 Likelihood" ].sum() ])

            return person7sum

        def person8stuff():
            stringlike = stringlikestuff()
            person8f = pd.DataFrame([ person8() ]).transpose()
            person8df = person8f.iloc[1:, :]
            person8likely = person8df.mul(stringlike.values)
            person8likely.columns = ["Person 8 Likelihood"]
            person8sum = pd.DataFrame([ person8likely[ "Person 8 Likelihood" ].sum() ])

            return person8sum

        def person9stuff():
            stringlike = stringlikestuff()
            person9f = pd.DataFrame([ person9() ]).transpose()
            person9df = person9f.iloc[1:, :]
            person9likely = person9df.mul(stringlike.values)
            person9likely.columns = ["Person 9 Likelihood"]
            person9sum = pd.DataFrame([ person9likely[ "Person 9 Likelihood" ].sum() ])

            return person9sum

        stringsum = stringsumstuff()
        famsum = famsumstuff()
        person1sum = person1stuff()
        person2sum = person2stuff()
        person3sum = person3stuff()
        person4sum = person4stuff()
        person5sum = person5stuff()
        person6sum = person6stuff()
        person7sum = person7stuff()
        person8sum = person8stuff()
        person9sum = person9stuff()

        ped1fhprob = person1sum.div(stringsum) * 100
        fh1prob = ped1fhprob.iloc[0, 0]
        # print(f"Person 1 Likelihood: {person1prob.iloc[0, 0]}%")

        ped2fhprob = person2sum.div(stringsum) * 100
        fh2prob = ped2fhprob.iloc[0, 0]
        # print(f"Person 2 Likelihood: {person2prob.iloc[0, 0]}%")

        ped3fhprob = person3sum.div(stringsum) * 100
        fh3prob = ped3fhprob.iloc[0, 0]
        # print(f"Person 3 Likelihood: {person3prob.iloc[0, 0]}%")

        ped4fhprob = person4sum.div(stringsum) * 100
        fh4prob = ped4fhprob.iloc[0, 0]
        # print(f"Person 4 Likelihood: {person4prob.iloc[0, 0]}%")

        ped5fhprob = person5sum.div(stringsum) * 100
        fh5prob = ped5fhprob.iloc[0, 0]
        # print(f"Person 5 Likelihood: {person5prob.iloc[0, 0]}%")

        ped6fhprob = person6sum.div(stringsum) * 100
        fh6prob = ped6fhprob.iloc[0, 0]
        # print(f"Person 6 Likelihood: {person6prob.iloc[0, 0]}%")

        ped7fhprob = person7sum.div(stringsum) * 100
        fh7prob = ped7fhprob.iloc[0, 0]
        # print(f"Person 7 Likelihood: {person7prob.iloc[0, 0]}%")

        ped8fhprob = person8sum.div(stringsum) * 100
        fh8prob = ped8fhprob.iloc[0, 0]
        # print(f"Person 8 Likelihood: {person8prob.iloc[0, 0]}%")

        ped9fhprob = person9sum.div(stringsum) * 100
        fh9prob = ped9fhprob.iloc[0, 0]

        test = fh9prob
        # print(test)
        # print(f"Person 9 Likelihood: {person9prob.iloc[0, 0]}%")

        familyprob = famsum.div(stringsum) * 100
        fhfamprob = familyprob.iloc[0,0]
        # print(f"Family Likelihood: {familyprob.iloc[0, 0]}%")

        fh1prob = float(fh1prob)
        fh2prob = float(fh2prob)
        fh3prob = float(fh3prob)
        fh4prob = float(fh4prob)
        fh5prob = float(fh5prob)
        fh6prob = float(fh6prob)
        fh7prob = float(fh7prob)
        fh8prob = float(fh8prob)
        fh9prob = float(fh9prob)

        dftable = pd.DataFrame(
            columns=["Pedigree Member", "Age", "LDL-C", "TOT-C", "Gender", "Clinical-CAD"
                , "CAD-Age", "TX-Status", "DNA-DX Status", "FH Probability", "Family Pedigree FH Probability"]

            ,data=[[ "Grandparent #1", ped1age, ped1ldlc, ped1totc, ped1gender
                    , ped1cadstat, ped1cadage, ped1tx, ped1dna, fh1prob, fhfamprob]

                , [ "Grandparent #2", ped2age, ped2ldlc, ped2totc, ped2gender
                    , ped2cadstat, ped2cadage, ped2tx, ped2dna, fh2prob ]

                , [ "Sibling #1", ped3age, ped3ldlc, ped3totc, ped3gender, ped3cadstat
                    , ped3cadage, ped3tx, ped3dna, fh3prob ]

                , [ "Sibling #2", ped4age, ped4ldlc, ped4totc, ped4gender, ped4cadstat
                    , ped4cadage, ped4tx, ped4dna, fh4prob ]

                , [ "Parent #1", ped5age, ped5ldlc, ped5totc, ped5gender, ped5cadstat
                    , ped5cadage, ped5tx, ped5dna, fh5prob ]

                , [ "Parent #2", ped6age, ped6ldlc, ped6totc, ped6gender, ped6cadstat
                    , ped6cadage, ped6tx, ped6dna, fh6prob ]

                , [ "Child #1", ped7age, ped7ldlc, ped7totc, ped7gender, ped7cadstat
                    , ped7cadage, ped7tx, ped7dna, fh7prob ]

                , [ "Child #2", ped8age, ped8ldlc, ped8totc, ped8gender, ped8cadstat
                    , ped8cadage, ped8tx, ped8dna, fh8prob ]

                , [ "Child #3", ped9age, ped9ldlc, ped9totc, ped9gender, ped9cadstat
                    , ped9cadage, ped9tx, ped9dna, fh9prob ]])

        filename = datetime.datetime.now().strftime("uploads/+%Y-%m-%d-%H-%M-%S-%f"+".csv")

        dftable.to_csv(filename, index = None, encoding = 'utf-8')

        # column_names = dftable.columns.values
        # row_data = list(dftable.values.tolist())

        # Final-formatting of person-probability of having FH before passing to index.html file
        fh1prob = "{:.1f}%".format(fh1prob)
        fh2prob = "{:.1f}%".format(fh2prob)
        fh3prob = "{:.1f}%".format(fh3prob)
        fh4prob = "{:.1f}%".format(fh4prob)
        fh5prob = "{:.1f}%".format(fh5prob)
        fh6prob = "{:.1f}%".format(fh6prob)
        fh7prob = "{:.1f}%".format(fh7prob)
        fh8prob = "{:.1f}%".format(fh8prob)
        fh9prob = "{:.1f}%".format(fh9prob)
        fhfamprob = "Family Pedigree FH Probability: {:.2f}%".format(fhfamprob) # Family-Pedigree formatting

        return render_template('calc/index.html', ped1age = ped1age, ped1ldlc = ped1ldlc, ped1totc = ped1totc
                               , ped1gender = ped1gender, ped1cadstat = ped1cadstat, ped1cadage = ped1cadage
                               , ped1tx = ped1tx, ped1dna = ped1dna, fh1prob = fh1prob, ped2age = ped2age
                               , ped2ldlc = ped2ldlc, ped2totc = ped2totc, ped2gender = ped2gender
                               , ped2cadstat = ped2cadstat, ped2cadage = ped2cadage, ped2tx = ped2tx, ped2dna = ped2dna
                               , fh2prob = fh2prob, ped3age = ped3age, ped4age = ped4age, ped5age = ped5age
                               , ped6age = ped6age, ped7age = ped7age, ped8age = ped8age, ped9age = ped9age
                               , ped3gender = ped3gender, ped4gender = ped4gender, ped5gender = ped5gender
                               , ped6gender = ped6gender, ped7gender = ped7gender, ped8gender = ped8gender, ped9gender = ped9gender
                               , ped3ldlc = ped3ldlc, ped4ldlc = ped4ldlc, ped5ldlc = ped5ldlc, ped6ldlc = ped6ldlc
                               , ped7ldlc = ped7ldlc, ped8ldlc = ped8ldlc, ped9ldlc = ped9ldlc
                               , ped3totc = ped3totc, ped4totc = ped4totc, ped5totc = ped5totc, ped6totc = ped6totc
                               , ped7totc = ped7totc, ped8totc = ped8totc, ped9totc = ped9totc
                               , ped3tx = ped3tx, ped4tx = ped4tx, ped5tx = ped5tx, ped6tx = ped6tx, ped7tx = ped7tx
                               , ped8tx = ped8tx, ped9tx = ped9tx
                               , ped3cadstat = ped3cadstat, ped4cadstat = ped4cadstat, ped5cadstat = ped5cadstat
                               , ped6cadstat = ped6cadstat, ped7cadstat = ped7cadstat, ped8cadstat = ped8cadstat
                               , ped9cadstat = ped9cadstat
                               , ped3cadage = ped3cadage, ped4cadage = ped4cadage, ped5cadage = ped5cadage
                               , ped6cadage = ped6cadage, ped7cadage = ped7cadage, ped8cadage = ped8cadage
                               , ped9cadage = ped9cadage
                               , ped3dna = ped3dna, ped4dna = ped4dna, ped5dna = ped5dna, ped6dna = ped6dna
                               , ped7dna = ped7dna, ped8dna = ped8dna, ped9dna = ped9dna
                               , fh3prob = fh3prob, fh4prob = fh4prob
                               , fh5prob = fh5prob, fh6prob = fh6prob, fh7prob = fh7prob, fh8prob = fh8prob
                               , fh9prob = fh9prob, fhfamprob = fhfamprob, btn = 'calc/download.html')

    else:
        return render_template('calc/index.html')

@app.route('/download-file/')
def download():

    # Name for File-downloaded by user. Using of datetime library to print time of user-download
    attachment_filename = datetime.datetime.now().strftime("FHResults-%Y-%m-%d-%H-%M-%S-%f"+".csv")
    return send_file(filename, attachment_filename = attachment_filename, as_attachment = True)

if __name__ == "__main__":
    app.run(debug = True)
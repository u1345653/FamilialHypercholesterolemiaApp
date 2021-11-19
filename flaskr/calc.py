from typing import Union, Any

from flask import Blueprint, flash, g, redirect, render_template, request, url_for, jsonify, json, app
from werkzeug.exceptions import abort
from werkzeug.datastructures import MultiDict

bp = Blueprint('calc', __name__)

# @bp.route('/_results', methods = ['POST', 'GET'])
# def results():
#     a = request.args.get('a', 0, type = int)
#     b = request.args.get('b', 0, type = int)
#     result = jsonify(result = a + b)
#     return render_template('calc/index.html', result = 1)

@bp.route('/', methods = ['GET', 'POST'])
def index():

    if request.method == "POST":

        form_data = request.form.get('results')

        # printform_data = jsonify(form_data)
        # print(printform_data)

        ###############################################################################
        # EXPERIMENTING W/ CONVERTING STRING TO JSON... FAILED TODO() - INSPECT LATER #
        ###############################################################################

        # form_data = request.form.getlist("results")
        # jsonform_data = jsonify(form_data).get_json()[0]
        # jsondumptest = json.dumps(jsonform_data)
        # print(type(jsondumptest))

        # for key, value in form_data:
        #     print("Key: ", key)
        #     print("Value: ", str(value))
        # jsonform_data = MultiDict([form_data]).lists()


        # var = jsonform_data

        # selectedPedigree = request.form.get("pedigreeChoice")

        # PEDIGREE 1'S DATA ATTRIBUTES
        ped1age = int(request.form.get("ped1Age"))
        ped1gender = request.form.get("ped1Gender")
        ped1ldlc = int(request.form.get("ped1LDLChol"))
        ped1totc = int(request.form.get("ped1TOTChol"))
        ped1tx = int(request.form.get("ped1TXStatus"))
        ped1cadstat = int(request.form.get("ped1CadStatus"))
        ped1cadage = int(request.form.get("ped1CadAge"))
        ped1dna = int(request.form.get("ped1DnaDxStatus"))
        # print("Pedigree 1 Test Attributes -\nAge: ", ped1age, "Dtype: ", type(ped1age),
        #       "\nGender: ", ped1gender, "Dtype: ", type(ped1gender), "\nLDL: ", ped1ldlc, "Dtype: ", type(ped1ldlc),
        #       "\nTOTC: ", ped1totc, "Dtype: ", type(ped1totc), "\nTX: ", ped1tx, "Dtype: ", type(ped1tx),
        #       "\nCAD-Status: ", ped1cadstat, "Dtype: ", type(ped1cadstat)
        #       , "\nCAD-AGE: ", ped1cadage, "Dtype", type(ped1cadage), "\nDNA-DX: ", ped1dna, "Dtype: ", type(ped1dna))


        # PEDIGREE 2'S DATA ATTRIBUTES
        ped2age = int(request.form.get("ped2Age"))
        ped2gender = request.form.get("ped2Gender")
        ped2ldlc = int(request.form.get("ped2LDLChol"))
        ped2totc = int(request.form.get("ped2TOTChol"))
        ped2tx = int(request.form.get("ped2TXStatus"))
        ped2cadstat = int(request.form.get("ped2CadStatus"))
        ped2cadage = int(request.form.get("ped2CadAge"))
        ped2dna = int(request.form.get("ped2DnaDxStatus"))
        # print("\n\nPedigree 2 Test Attributes -\nAge: ", ped2age, "Dtype: ", type(ped2age),
        #       "\nGender: ", ped2gender, "Dtype: ", type(ped2gender), "\nLDL: ", ped2ldlc, "Dtype: ", type(ped2ldlc),
        #       "\nTOTC: ", ped2totc, "Dtype: ", type(ped2totc), "\nTX: ", ped2tx, "Dtype: ", type(ped2tx),
        #       "\nCAD-Status: ", ped2cadstat, "Dtype: ", type(ped2cadstat)
        #       , "\nCAD-AGE: ", ped2cadage, "Dtype", type(ped2cadage), "\nDNA-DX: ", ped2dna, "Dtype: ", type(ped2dna))


        # PEDIGREE 3'S DATA ATTRIBUTES
        ped3age = int(request.form.get("ped3Age"))
        ped3gender = request.form.get("ped3Gender")
        ped3ldlc = int(request.form.get("ped3LDLChol"))
        ped3totc = int(request.form.get("ped3TOTChol"))
        ped3tx = int(request.form.get("ped3TXStatus"))
        ped3cadstat = int(request.form.get("ped3CadStatus"))
        ped3cadage = int(request.form.get("ped3CadAge"))
        ped3dna = int(request.form.get("ped3DnaDxStatus"))
        # print("\n\nPedigree 3 Test Attributes -\nAge: ", ped3age, " Dtype:", type(ped3age),
        #       "\nGender:", ped3gender, " Dtype:", type(ped3gender), "\nLDL:", ped3ldlc, " Dtype:", type(ped3ldlc),
        #       "\nTOTC:", ped3totc, " Dtype:", type(ped3totc), "\nTX:", ped3tx, " Dtype:", type(ped3tx),
        #       "\nCAD-Status:", ped3cadstat, " Dtype:", type(ped3cadstat)
        #       , "\nCAD-AGE:", ped3cadage, " Dtype", type(ped3cadage), "\nDNA-DX:", ped3dna, " Dtype:", type(ped3dna))


        # PEDIGREE 4'S DATA ATTRIBUTES
        ped4age = int(request.form.get("ped4Age"))
        ped4gender = request.form.get("ped4Gender")
        ped4ldlc = int(request.form.get("ped4LDLChol"))
        ped4totc = int(request.form.get("ped4TOTChol"))
        ped4tx = int(request.form.get("ped4TXStatus"))
        ped4cadstat = int(request.form.get("ped4CadStatus"))
        ped4cadage = int(request.form.get("ped4CadAge"))
        ped4dna = int(request.form.get("ped4DnaDxStatus"))
        # print("\n\nPedigree 4 Test Attributes -\nAge: ", ped4age, " Dtype:", type(ped4age),
        #       "\nGender:", ped4gender, " Dtype:", type(ped4gender), "\nLDL:", ped4ldlc, " Dtype:", type(ped4ldlc),
        #       "\nTOTC:", ped4totc, " Dtype:", type(ped4totc), "\nTX:", ped4tx, " Dtype:", type(ped4tx),
        #       "\nCAD-Status:", ped4cadstat, " Dtype:", type(ped4cadstat)
        #       , "\nCAD-AGE:", ped4cadage, " Dtype", type(ped4cadage), "\nDNA-DX:", ped4dna, " Dtype:", type(ped4dna))


        # PEDIGREE 5'S DATA ATTRIBUTES
        ped5age = int(request.form.get("ped5Age"))
        ped5gender = request.form.get("ped5Gender")
        ped5ldlc = int(request.form.get("ped5LDLChol"))
        ped5totc = int(request.form.get("ped5TOTChol"))
        ped5tx = int(request.form.get("ped5TXStatus"))
        ped5cadstat = int(request.form.get("ped5CadStatus"))
        ped5cadage = int(request.form.get("ped5CadAge"))
        ped5dna = int(request.form.get("ped5DnaDxStatus"))
        # print("\n\nPedigree 5 Test Attributes -\nAge: ", ped5age, " Dtype:", type(ped5age),
        #       "\nGender:", ped5gender, " Dtype:", type(ped5gender), "\nLDL:", ped5ldlc, " Dtype:", type(ped5ldlc),
        #       "\nTOTC:", ped5totc, " Dtype:", type(ped5totc), "\nTX:", ped5tx, " Dtype:", type(ped5tx),
        #       "\nCAD-Status:", ped5cadstat, " Dtype:", type(ped5cadstat)
        #       , "\nCAD-AGE:", ped5cadage, " Dtype", type(ped5cadage), "\nDNA-DX:", ped5dna, " Dtype:", type(ped5dna))


        # PEDIGREE 6'S DATA ATTRIBUTES
        ped6age = int(request.form.get("ped6Age"))
        ped6gender = request.form.get("ped6Gender")
        ped6ldlc = int(request.form.get("ped6LDLChol"))
        ped6totc = int(request.form.get("ped6TOTChol"))
        ped6tx = int(request.form.get("ped6TXStatus"))
        ped6cadstat = int(request.form.get("ped6CadStatus"))
        ped6cadage = int(request.form.get("ped6CadAge"))
        ped6dna = int(request.form.get("ped6DnaDxStatus"))
        # print("\n\nPedigree 6 Test Attributes -\nAge: ", ped6age, " Dtype:", type(ped6age),
        #       "\nGender:", ped6gender, " Dtype:", type(ped6gender), "\nLDL:", ped6ldlc, " Dtype:", type(ped6ldlc),
        #       "\nTOTC:", ped6totc, " Dtype:", type(ped6totc), "\nTX:", ped6tx, " Dtype:", type(ped6tx),
        #       "\nCAD-Status:", ped6cadstat, " Dtype:", type(ped6cadstat)
        #       , "\nCAD-AGE:", ped6cadage, " Dtype", type(ped6cadage), "\nDNA-DX:", ped6dna, " Dtype:", type(ped6dna))


        # PEDIGREE 7'S DATA ATTRIBUTES
        ped7age = int(request.form.get("ped7Age"))
        ped7gender = request.form.get("ped7Gender")
        ped7ldlc = int(request.form.get("ped7LDLChol"))
        ped7totc = int(request.form.get("ped7TOTChol"))
        ped7tx = int(request.form.get("ped7TXStatus"))
        ped7cadstat = int(request.form.get("ped7CadStatus"))
        ped7cadage = int(request.form.get("ped7CadAge"))
        ped7dna = int(request.form.get("ped7DnaDxStatus"))
        # print("\n\nPedigree 7 Test Attributes -\nAge: ", ped7age, " Dtype:", type(ped7age),
        #       "\nGender:", ped7gender, " Dtype:", type(ped7gender), "\nLDL:", ped7ldlc, " Dtype:", type(ped7ldlc),
        #       "\nTOTC:", ped7totc, " Dtype:", type(ped7totc), "\nTX:", ped7tx, " Dtype:", type(ped7tx),
        #       "\nCAD-Status:", ped7cadstat, " Dtype:", type(ped7cadstat)
        #       , "\nCAD-AGE:", ped7cadage, " Dtype", type(ped7cadage), "\nDNA-DX:", ped7dna, " Dtype:", type(ped7dna))


        # PEDIGREE 8'S DATA ATTRIBUTES
        ped8age = int(request.form.get("ped8Age"))
        ped8gender = request.form.get("ped8Gender")
        ped8ldlc = int(request.form.get("ped8LDLChol"))
        ped8totc = int(request.form.get("ped8TOTChol"))
        ped8tx = int(request.form.get("ped8TXStatus"))
        ped8cadstat = int(request.form.get("ped8CadStatus"))
        ped8cadage = int(request.form.get("ped8CadAge"))
        ped8dna = int(request.form.get("ped8DnaDxStatus"))
        # print("\n\nPedigree 8 Test Attributes -\nAge: ", ped8age, " Dtype:", type(ped8age),
        #       "\nGender:", ped8gender, " Dtype:", type(ped8gender), "\nLDL:", ped8ldlc, " Dtype:", type(ped8ldlc),
        #       "\nTOTC:", ped8totc, " Dtype:", type(ped8totc), "\nTX:", ped8tx, " Dtype:", type(ped8tx),
        #       "\nCAD-Status:", ped8cadstat, " Dtype:", type(ped8cadstat)
        #       , "\nCAD-AGE:", ped8cadage, " Dtype", type(ped8cadage), "\nDNA-DX:", ped8dna, " Dtype:", type(ped8dna))


        # PEDIGREE 9'S DATA ATTRIBUTES
        ped9age = int(request.form.get("ped9Age"))
        ped9gender = request.form.get("ped9Gender")
        ped9ldlc = int(request.form.get("ped9LDLChol"))
        ped9totc = int(request.form.get("ped9TOTChol"))
        ped9tx = int(request.form.get("ped9TXStatus"))
        ped9cadstat = int(request.form.get("ped9CadStatus"))
        ped9cadage = int(request.form.get("ped9CadAge"))
        ped9dna = int(request.form.get("ped9DnaDxStatus"))
        # print("\n\nPedigree 9 Test Attributes -\nAge: ", ped9age, " Dtype:", type(ped9age),
        #       "\nGender:", ped9gender, " Dtype:", type(ped9gender), "\nLDL:", ped9ldlc, " Dtype:", type(ped9ldlc),
        #       "\nTOTC:", ped9totc, " Dtype:", type(ped9totc), "\nTX:", ped9tx, " Dtype:", type(ped9tx),
        #       "\nCAD-Status:", ped9cadstat, " Dtype:", type(ped9cadstat)
        #       , "\nCAD-AGE:", ped9cadage, " Dtype", type(ped9cadage), "\nDNA-DX:", ped9dna, " Dtype:", type(ped9dna))


        return render_template('calc/index.html')

    else:
        return render_template('calc/index.html')

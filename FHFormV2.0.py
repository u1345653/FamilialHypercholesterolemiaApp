########################################################################################################################
###                       PURPOSE: TRANSPOSE V1.0 OF THE FH FORM INTO THE LAYOUT.HTML, THEN CSS PAGE                 ###
###                         TITLE: FH-CAPSTONE PROJECT WEBSITE: ACCEPTING USER INPUTS VIA A FORM                     ###
###                                                     VERSION: 2                                                   ###
###                                                   DATE: 9.29.21                                                  ###
########################################################################################################################
###                                                    DEPENDENCIES                                                  ###
###                         1) 'PIP INSTALL FLASK' VIA CMD TO INSTALL FLASK LIBRARY                                  ###
###                2) PYTHON CODE TRANSPOSED TO WEB SERVER AND PRESENTED TO WEBPAGE VIA PYTHONEVERYWHERE.COM         ###
###   3) .PY FILES & .HTML FILES ARE BUILT OUT CORRECTLY AND HAVE BEEN TESTED TO REFERENCE EACHOTHER APPROPRIATELY   ###
###                4) EXPERIENCE/ IMPLEMENTATION OF THE FHFORMV1.0.PY FILE... BASIC HTML FORM ALREADY MADE           ###
########################################################################################################################
#                                       STEP 1 - IMPORTING NECESSARY LIBRARIES                                         #
########################################################################################################################

# IMPORTING RENDER_TEMPLATE FOR PURPOSES OF .HTML TEMPLATE CONNECTIVITY
# IMPORTING FLASK CLASS TO CREATE FLASK OBJECT, 'APP'
# IMPORTING REQUEST OBJECT, TO FACILITATE THE 'GET' & 'POST' METHODS FOR USER INPUT DATA.
from flask import Flask, render_template, request

from werkzeug.datastructures import ImmutableMultiDict

app = Flask(__name__)  # CREATING VARIABLE THAT REPRESENTS THE INSTANTIATED FLASK OBJECT, 'APP'.


########################################################################################################################
#                                       STEP 2 - CREATING OUR DESIRED WEBPAGES                                         #
########################################################################################################################

# ADDITION #1 - ADDING A DEFAULT PAGE TO ACCOUNT FOR NOTHING AFTER BACKSLASH (PRIMARILY TO SPEED UP TESTING)
@app.route('/')  # PAGE 1 - ''FORM'' - INCLUDING '/' AS PARAMETER SIGNIFIES A DEFAULT URL
def home():  # FUNCTION FOR PAGE 1 - RENDERING THE 'HOME.TML' TEMPLATE
    return render_template('form.html')


@app.route('/form')  # PAGE 2 '/FORM' - PAGE THAT PRESENTS ITSELF AS A FORM FOR USER INPUT
def form():  # FUNCTION FOR PAGE 2 - RENDERING THE 'FORM.HTML' TEMPLATE
    return render_template('form.html')


@app.route('/data/'  # PAGE 3 '/DATA/' - PAGE THAT PERFORMS DATA CALCULATIONS FROM USER INPUT
    , methods=['POST', 'GET'])  # DEFINING OUR @APP.ROUTE() METHOD ARGUMENTS, 'POST' & 'GET' FOR DATA MANIPULATION
def data():  # FUNCTION FOR PAGE 3 - HANDLES THE 'GETTING' & 'POSTING' OF USER INPUT

    if request.method == 'GET':  # CONDITIONAL STATEMENT 1 - 'GETTING' STATEMENT, RETURNING PRINT
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"

    if request.method == 'POST':  # CONDITIONAL STATEMENT 2 - 'POSTING' STATEMENT, RETURNING THE RENDERING OF OUR 'DATA.HTML' TEMPLATE
        form_data: ImmutableMultiDict[str, str] = request.form
        return render_template('data.html',
                               form_data=form_data)


@app.route('/about/')
def about():
    return render_template('about.html')


########################################################################################################################
#                             STEP 3 - CREATING CONDITION WHICH INITIATES THE FLASK SESSION                            #
########################################################################################################################

if __name__ == "__main__":  # IF __NAME__ PARAMETER == "__MAIN__", THEN WE WANT OUR APP TO START
    app.run(debug=False)  # APP.RUN() METHOD, WHICH STARTS OUR FLASK OBJECT'S SESSION

#### NOTE - IF USING ON YOUR OWN LOCAL CLIENT FOR TESTING PURPOSES, COMMENT OUT LINES 42-43, AND USE THE FOLLOWING
# APP.RUN() METHOD INSTEAD TO TEST FLASK ENVIRONMENT ON LOCAL DEVICE VIA PORT 5000.

# app.run(host='localhost'  # ARGUMENT 1 - HOST = 'LOCALHOST'; DEFINING THE HOST OF FLASK SESSION
#         , port=5000)  # ARGUMENT 2 - PORT = '5000'; DEFINING THE PORT ALLOWING FOR WEB-BROWSER SESSION

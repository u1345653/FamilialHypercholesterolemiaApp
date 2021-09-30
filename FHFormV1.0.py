########################################################################################################################
###                         PURPOSE: CREATE A DRAFT FORM FOR USER INPUT VARIABLES FOR FH PROJECT                     ###
###                         TITLE: FH-CAPSTONE PROJECT WEBSITE: ACCEPTING USER INPUTS VIA A FORM                     ###
###                                                     VERSION: 1                                                   ###
###                                                   DATE: 9.29.21                                                  ###
########################################################################################################################
###                                                    DEPENDENCIES                                                  ###
###                         1) 'PIP INSTALL FLASK' VIA CMD TO INSTALL FLASK LIBRARY                                  ###
###                2) PYTHON CODE TRANSPOSED TO WEB SERVER AND PRESENTED TO WEBPAGE VIA PYTHONEVERYWHERE.COM         ###
###   3) .PY FILES & .HTML FILES ARE BUILT OUT CORRECTLY AND HAVE BEEN TESTED TO REFERENCE EACHOTHER APPROPRIATELY   ###
########################################################################################################################
#                                       STEP 1 - IMPORTING NECESSARY LIBRARIES                                         #
########################################################################################################################

from flask import (Flask  # IMPORTING FLASK CLASS TO CREATE FLASK OBJECT, 'APP'
, render_template  # IMPORTING RENDER_TEMPLATE FOR PURPOSES OF .HTML TEMPLATE CONNECTIVITY
, request)  # IMPORTING REQUEST OBJECT, TO FACILITATE THE 'GET' & 'POST' METHODS FOR USER INPUT DATA.
from werkzeug.datastructures import ImmutableMultiDict

app = Flask(__name__)  # CREATING VARIABLE THAT REPRESENTS THE INSTANTIATED FLASK OBJECT, 'APP'.


########################################################################################################################
#                                       STEP 2 - CREATING OUR DESIRED WEBPAGES                                         #
########################################################################################################################

@app.route('/form')  # PAGE 1 '/FORM' - PAGE THAT PRESENTS ITSELF AS A FORM FOR USER INPUT
def form():  # FUNCTION FOR PAGE 1 - RENDERING THE 'FORM.HTML' TEMPLATE
    return render_template('fhtemplates/form.html')


@app.route('/data/'  # PAGE 2 '/DATA/' - PAGE THAT PERFORMS DATA CALCULATIONS FROM USER INPUT
    , methods=['POST', 'GET'])  # DEFINING OUR @APP.ROUTE() METHOD ARGUMENTS, 'POST' & 'GET' FOR DATA MANIPULATION
def data():  # FUNCTION FOR PAGE 2 - HANDLES THE 'GETTING' & 'POSTING' OF USER INPUT

    if request.method == 'GET':  # CONDITIONAL STATEMENT 1 - 'GETTING' STATEMENT, RETURNING PRINT
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"

    if request.method == 'POST':  # CONDITIONAL STATEMENT 2 - 'POSTING' STATEMENT, RETURNING THE RENDERING OF OUR 'DATA.HTML' TEMPLATE
        form_data: ImmutableMultiDict[str, str] = request.form
        return render_template('fhtemplates/data.html',
                               form_data=form_data)


########################################################################################################################
#                             STEP 3 - CREATING CONDITION WHICH INITIATES THE FLASK SESSION                            #
########################################################################################################################

# if __name__ == "__main__":                     # IF __NAME__ PARAMETER == "__MAIN__", THEN WE WANT OUR APP TO START
#    app.run(debug=True)                        # APP.RUN() METHOD, WHICH STARTS OUR FLASK OBJECT'S SESSION

#### NOTE - IF USING ON YOUR OWN LOCAL CLIENT FOR TESTING PURPOSES, COMMENT OUT LINES 42-43, AND USE THE FOLLOWING
# APP.RUN() METHOD INSTEAD TO TEST FLASK ENVIRONMENT ON LOCAL DEVICE VIA PORT 5000.

app.run(host='localhost'  # ARGUMENT 1 - HOST = 'LOCALHOST'; DEFINING THE HOST OF FLASK SESSION
        , port=5000)  # ARGUMENT 2 - PORT = '5000'; DEFINING THE PORT ALLOWING FOR WEB-BROWSER SESSION

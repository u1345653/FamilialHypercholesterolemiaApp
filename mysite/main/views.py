########################################################################################################################
###                            VIEWS FILE FOR CREATING DIFFERENT VIEWS OF OUR APPLICATION                            ###
###                         PURPOSE: TRANSPOSING FH CALCULATOR FRAMEWORK TO DJANGO WEB APP                           ###
###                                        DATE: 9.30.21 ---- VERSION: 1.0                                           ###
########################################################################################################################
###                VIEWS PAGE IS WHERE WE WILL DEVELOP OUR HTTPS REQUESTS FOR VIEWS ON OUR WEB APPLICATION           ###

### STEP 1 - IMPORTING DJANGO LIBRARY'S & CLASSES FOR PT. 1
from django.shortcuts import render
from django.http import HttpResponse            # ALLOWS US TO SERVE AND MANAGE VIEWS DEFINE BELOW TO CORRESPONDING URLS


### STEP 2 - CREATE AND DEFINE FUNCTION THAT WILL REPRESENT A VEW
def index(response):
    return HttpResponse("<h2>FH Calc Test</h2>")

def v1(response):
    return HttpResponse("<h3>View #1</h3>")
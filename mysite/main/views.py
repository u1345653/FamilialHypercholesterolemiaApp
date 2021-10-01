########################################################################################################################
###                            VIEWS FILE FOR CREATING DIFFERENT VIEWS OF OUR APPLICATION                            ###
###                         PURPOSE: TRANSPOSING FH CALCULATOR FRAMEWORK TO DJANGO WEB APP                           ###
###                                        DATE: 9.30.21 ---- VERSION: 3.0                                           ###
########################################################################################################################
###                VIEWS PAGE IS WHERE WE WILL DEVELOP OUR HTTPS REQUESTS FOR VIEWS ON OUR WEB APPLICATION           ###

### STEP 1 - IMPORTING DJANGO LIBRARY'S & CLASSES FOR PT. 1
from django.shortcuts import render
from django.http import HttpResponse         # LIBRARY THAT MAPS VIEWS DEFINED IN FUNCTIONS BELOW TO CORRESPONDING PAGES
from .models import ToDoList, Item           # IMPORT OUR MODELS TODOLIST/ ITEM, TO 'GET' THE TODOLIST FROM THE ID


### STEP 2 - CREATE DYNAMIC FUNCTION REPRESENTS A VIEW; NOTE THE INCLUSION OF ADDITIONAL PARAMETER FOR DYNAMIC ABILITY
# DYNAMIC EX1: PASSING OBJECT'S 'NAME' ATTRIBUTE FROM THE TODOLIST CLASS THROUGH FUNCTION
# , THEN GETTING & PRINTING IT & ASSOCIATED ATTRIBUTES ON THE CORRESPONDING WEBPAGE.

def index(response                                # PASSING THE HTTP RESPONSE INTO OUR INDEX FUNCTION
          , id):                                  # PASSING THE UNIQUE TODOLIST ID THROUGH OUR INDEX FUNCTION

    ls = ToDoList.objects.get(id=id)

    # RETURNING AN INSTANCE OF THE RENDER CLASS, WHICH GENERATES THE HTML FILE DESCRIBED
    return render( response
                  , "main/list.html"
                  , {"ls" : ls} )

## DYNAMIC EX2: PASSING THE 'NAME' ATTRIBUTE FROM THE TODOLIST CLASS, THEN GETTING & PRINTING IT DYNAMICALLY
# IF USER TYPES IN 'TIM'S LIST' AT END OF URL, WE CAN USE THAT TO DISPLAY THE NAME OF THAT TODOLIST OBJECT ON PAGE
# def index(response
#     , name)
#     name = ToDoList.objects.get(name=name)
#     return HttpResponse("<h1>%s</h1>" % ls.name)

def home(response):
    return render( response
                  , "main/home.html"
                  , {} )
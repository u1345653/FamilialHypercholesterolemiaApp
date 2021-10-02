########################################################################################################################
###                            VIEWS FILE FOR CREATING DIFFERENT VIEWS OF OUR APPLICATION                            ###
###                         PURPOSE: TRANSPOSING FH CALCULATOR FRAMEWORK TO DJANGO WEB APP                           ###
###                                        DATE: 10.1.21 ---- VERSION: 4.0                                           ###
########################################################################################################################
###                VIEWS PAGE IS WHERE WE WILL DEVELOP OUR HTTPS REQUESTS FOR VIEWS ON OUR WEB APPLICATION           ###

### STEP 1 - IMPORTING DJANGO LIBRARY'S & CLASSES FOR PT. 1
from django.shortcuts import render
from django.http import (HttpResponse        # LIBRARY THAT MAPS VIEWS DEFINED IN FUNCTIONS BELOW TO CORRESPONDING PAGES
    , HttpResponseRedirect)                  # ALLOWS US TO SHOW A RESPONSE REDIRECT WITHIN OUR BROWSER
from .models import ToDoList, Item           # IMPORT OUR MODELS TODOLIST/ ITEM, TO 'GET' THE TODOLIST FROM THE ID
from .forms import CreateNewList             # IMPORT OUR FORMS OBJECT, TO PASS THE FORM OBJECT INTO OUR HTML CODE


### STEP 2 - CREATE DYNAMIC FUNCTION REPRESENTS A VIEW; NOTE THE INCLUSION OF ADDITIONAL PARAMETER FOR DYNAMIC ABILITY
# DYNAMIC EX1: PASSING OBJECT'S 'NAME' ATTRIBUTE FROM THE TODOLIST CLASS THROUGH FUNCTION
# , THEN GETTING & PRINTING IT & ASSOCIATED ATTRIBUTES ON THE CORRESPONDING WEBPAGE.

def index(response                                # PASSING THE HTTP RESPONSE INTO OUR INDEX FUNCTION
          , id):                                  # PASSING THE UNIQUE TODOLIST ID THROUGH OUR INDEX FUNCTION

    ls = ToDoList.objects.get(id=id)

    if response.method == "POST":                 # CONDITIONAL HANDLING LOGIC OF USER INPUT FORM ITEMS
        print(response.POST)                      # TEMPORARILY PRINTING THE POSTED RESPONSE FOR TESTING

        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True

                else:
                    item.complete = False

                item.save()

        elif response.POST.get("newItem"):
            txt = response.POST.get("new")

            if len(txt) > 2:
                ls.item_set.create(text=txt,
                                   complete = False)
            else:
                print("invalid")

            pass

    return render( response                 # FUNCTION 1 - RENDERING LIST.HTML FILE
                  , "main/list.html"
                  , {"ls" : ls} )

## DYNAMIC EX2: PASSING THE 'NAME' ATTRIBUTE FROM THE TODOLIST CLASS, THEN GETTING & PRINTING IT DYNAMICALLY
# IF USER TYPES IN 'TIM'S LIST' AT END OF URL, WE CAN USE THAT TO DISPLAY THE NAME OF THAT TODOLIST OBJECT ON PAGE
# def index(response
#     , name)
#     name = ToDoList.objects.get(name=name)
#     return HttpResponse("<h1>%s</h1>" % ls.name)


def home(response):                          # FUNCTION 2 - RENDERING HOME.HTML FILE
    return render( response
                  , "main/home.html"
                  , {} )

def create(response):                        # FUNCTION 3 - RENDERING CREATE.HTML FILE

    if response.method == "POST":                     # CONDITIONAL STATEMENT FOR 'POST' METHOD
        form = CreateNewList(response.POST)           # HOLDS A DICTIONARY THAT SAVES THE VALUES THE USER TYPES IN THEM

        if form.is_valid():                            # CONDITIONAL STATEMENT FOR IF THE FORM INFO IS VALID
            n = form.cleaned_data["name"]              # CREATING A VALID THAT CLEANS THE DATA WITH AN ENTRY IN OUR FORM
            t = ToDoList(name=n)
            t.save()

        return HttpResponseRedirect("/%i" %t.id)          # RETURNING VALUE OF USERS FORM INPUT FOR THEM TO VIEW

    else:
        form = CreateNewList()                             # CALLING THE CREATED CLASS, SINCE OUTPUT IS DEPENDENT ON IT
    return render ( response
                    , "main/create.html"
                    , {"form" : form } )
########################################################################################################################
###                     URLS FILE FOR REPRESENTING THE DIFFERENT ADDRESSES WE SERVE VIEWS TO                         ###
###                     PURPOSE: MODIFYING THE URLS TO ACCOMMODATE A FICTIONAL USER REGISTER                         ###
###                                        DATE: 10.1.21 ---- VERSION: 3.0                                           ###
########################################################################################################################
###                URLS PAGE IS WHERE WE WILL DEFINE THE PATHS TO OUR DIFFERENT WEB APP WEB PAGES.
###                LISTED URLS WILL DEFINE WHICH VIEWS ARE USED BASED ON GIVEN VIEWS WE WANT, AS WE DETERMINE

### STEP 1 - URLS LIBRARY AND IMPORTING PATH, THEN ALSO IMPORTING OUR VIEWS FILE. FROM THERE, WE CAN START
# TO MAP OUT DESIRED USER/URL PATHS BASED UPON HOW WE DEFINE OUR VARIABLES

from django.urls import path
from . import views
from fhcalc import views as v

### STEP 2 - DEFINING THE URL BEHAVIOR FOR WHEN A PATH DOES NOT INCLUDE ANY TEXT; AKA: OUR DEFAULT.
#  'PATH' PARAMETERS DEFINED IN THIS ITEM, EACH REPRESENT A MAPPING TO A FUNCTION IN OUR VIEWS FILE
urlpatterns = [

    # DEFINING PATH 1 - INDEX PAGE
    path("<int:id>"            # INCLUDING '<>' IN OUR ARGUMENT ALLOWS US TO READ PATH DYNAMICALLY FROM URL INPUT
         , views.index         # THE VIEW WE'RE REFERENCING
         , name="index"),      # THE NAME OF THE VIEW WE'RE CREATING; MAPS BACK TO THE FUNCTION NAME ""

    # DEFINING PATH 2 - HOME PAGE -- NOTE THAT "" AS THE LEADING ARGUMENT TELLS US THIS IS THE DEFAULT URL PATH
    path("about/"
         , views.home
         , name="about"),

    # PATH 3 - CREATE PAGE -- ALLOWING USERS TO CREATE  & VIEW LISTS
    path("create/"
         , views.create
         , name="create"),

    # PATH 4 - FHCALCULATOR PAGE
    path("fhcalc/", v.fhcalc, name = "fhcalc"),

    path('', v.fhcalc, name = "fhcalc"),

]
########################################################################################################################
###                     URLS FILE FOR REPRESENTING THE DIFFERENT ADDRESSES WE SERVE VIEWS TO                         ###
###                         PURPOSE: TRANSPOSING FH CALCULATOR FRAMEWORK TO DJANGO WEB APP                           ###
###                                        DATE: 9.30.21 ---- VERSION: 1.0                                           ###
########################################################################################################################
###                URLS PAGE IS WHERE WE WILL DEFINE THE PATHS TO OUR DIFFERENT WEB APP WEB PAGES.
###                LISTED URLS WILL DEFINE WHICH VIEWS ARE USED BASED ON GIVEN VIEWS WE WANT, AS WE DETERMINE

### STEP 1 - URLS LIBRARY AND IMPORTING PATH, THEN ALSO IMPORTING OUR VIEWS FILE. FROM THERE, WE CAN START
# TO MAP OUT DESIRED USER/URL PATHS BASED UPON HOW WE DEFINE OUR VARIABLES

from django.urls import path
from . import views

### STEP 2 - DEFINING THE URL BEHAVIOR FOR WHEN A PATH DOES NOT INCLUDE ANY TEXT; AKA: OUR DEFAULT.
urlpatterns = [                               # PARAMETERS DEFINED IN THIS AREA, CONNECT TO THE VIEWS IN THE VIEW.PY FILE
    path("", views.index, name="index"),      # VIEW #1: INDEX PAGE
    path("v1/", views.v1, name="view 1"),      # VIEW #2: VIEW #1 PAGE
]
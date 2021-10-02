########################################################################################################################
###                                            DJANGO ADMIN DASHBOARD PYTHON FILE                                    ###
###                  PURPOSE: MODIFYING OUR DJANGO ADMIN CONFIG TO SHOW USERS, DATABASES, ETC.                       ###
###                                        DATE: 9.30.21 ---- VERSION: 1.0                                           ###
########################################################################################################################
###         ADMIN PAGE ALLOWS US TO DISPLAY THE USERS, DATABASES, AND OTHER OBJECTS WITHIN OUR ENVIRONMENT           ###
#
# A COMMON EXAMPLE IS THAT WE CAN CREATE A DATABASE OF OBJECTS, OR WORDS, ETC. THAT COULD BE PERFECTLY FUNCTIONAL      #
# IN OUR SCRIPT, BUT IT WOULDN'T DISPLAY IN OUR ADMIN DASHBOARD UNTIL IT WAS ADDED IN THIS PYTHON FILE.                #

# STEP 1 - IMPORTING NECESSARY ADMIN DJANGO LIBRARY MODULES & ANY CLASSES FROM THE OBJECTS WE MAY HAVE CREATED

from django.contrib import admin # STANDARD DJANGO ADMIN MODULE IMPORT
from .models import ToDoList     # IMPORTING THE TODOLIST CLASS THAT ALLOWS US TO REGISTER THIS DATA MODEL IN ADMIN VIEW
from .models import Item

# STEP 2 - INSTANTIATING OUR ADMIN OBJECT THE DESIRED DATA MODELS, WHICH ARE THEN TRANSPOSED TO OUR ADMIN DASHBOARD
admin.site.register(ToDoList)     # DATA MODEL 1 - TODOLIST OBJECT
admin.site.register(Item)         # DATA MODEL 2 - ITEM OBJECT
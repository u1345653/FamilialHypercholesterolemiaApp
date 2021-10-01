########################################################################################################################
###               MODELS.PY IS USED TO CONFIGURE ANY DATA MODELS WE WANT TO INCORPORATE INTO OUR WEBSITE             ###
###               PURPOSE: CREATE FIRST DRAFT OF DATA MODEL, TO EVENTUALLY INCLUDE THE FH CALC DATA MODEL            ###
###                                             VERSION: 1.0; DATE: 9.28.21                                          ###
########################################################################################################################

### STEP 1 - IMPORT DJANGO'S MODELS CLASS, WHICH ALLOWS US TO BUILD DATA MODEL CLASSES TO TRANSPOSE TO WEB APP
# IMPORTANT TO NOTE THAT THE 'MODELS' MODULE WILL ALLOW US TO CALL THE '.MODELS' CLASS, WHICH IS ESSENTIAL TO BUILDING
#   AND DEFINING OUR DATA MODELS
from django.db import models

### STEP 2 - CREATING THE CLASSES OF DATA OBJECTS THAT WILL COMPRISE OF THE OBJECTS WE WANT USERS TO INTERACT
# WITH ON OUR PAGES


# DRAFT CLASS 1 - CREATION OF A TODOLIST CLASS
class ToDoList(models.Model):                     # WITHIN EACH CREATED CLASS, WE MUST DEFINE OUR ATTRIBUTES
    name = models.CharField(max_length=200)       # ATTRIBUTE 1: 'NAME', DEFINED AS A CHARACTER FIELD W/ A LENGTH

    # WITHIN EACH DATA OBJECT, WE WILL DEFINE A FUNCTION THAT RETURNS THE STRING VALUE OF WHAT USER DEFINES
    # PRIMARILY USING AT FIRST FOR DEBUGGING.
    def __str__(self):
        return self.name

# DRAFT CLASS 2 - CREATION OF AN ITEMS CLASS; WHICH REQUIRES FOREIGN KEY DUE TO DESIRED FLOW OF DATA...
# WE REQUIRE A TODOLIST BEFORE AN ITEM INSTANTIATING OUR TODOLIST OBJECT... THEREFORE, WE MUST DEFINE THIS CLASSES
# ATTRIBUTE AS A FOREIGN KEY TO THE TODOLIST CLASS ABOVE.
class Item(models.Model):
    todolist = models.ForeignKey(ToDoList                     # ATTRIBUTE 1: 'TODOLIST', WHICH IS THE FOREIGNKEY
                                 , on_delete=models.CASCADE)  # DEFINING THE DESIRED BEHAVIOR OF OUR ATTRIBUTE

    text = models.CharField(max_length=300)                   # ATTRIBUTE 2: 'TEXT', AS A CHARACTER FIELD
    complete = models.BooleanField()                          # ATTRIBUTE 3: 'COMPLETE', AS A BOOLEAN FIELD

    # WITHIN EACH DATA OBJECT, WE WILL DEFINE A FUNCTION THAT RETURNS THE STRING VALUE OF WHAT USER DEFINES
    # PRIMARILY USING AT FIRST FOR DEBUGGING.
    def __str__(self):
        return self.text
########################################################################################################################
###               FORMS.PY IS USED TO CREATE OUR WEBSITE FORM OBJECT, TO PASS THROUGH .HTML FILES DYNAMICALLY        ###
###                PURPOSE: CREATE DRAFT OF DYNAMIC WEBSITE VARIABLE FORMS OBJECT, TO BUILD ON FOR CAPSTONE          ###
###                                             VERSION: 1.0; DATE: 9.30.21                                          ###
########################################################################################################################

## STEP 1 - IMPORT THE FORMS CLASS FROM THE DJANGO LIBRARY
from django import forms

## STEP 2 - CREATE A CLASS, WHICH WILL CONTAIN THE FORM OBJECTS ATTRIBUTES (AKA: FORM FIELDS)
class CreateNewList(forms.Form):

    ## REFERENCE DJANGO WEBSITE FOR EXTENSIVE FORM FIELD OPTIONS:
    # https://docs.djangoproject.com/en/3.1/topics/forms/#field-data

    name = forms.CharField(label="Name"                      # ATTRIBUTE 1 - NAME
                           , max_length = 200)

    check = forms.BooleanField(required=False)                # ATTRIBUTE 2 - CHECK BUTTON
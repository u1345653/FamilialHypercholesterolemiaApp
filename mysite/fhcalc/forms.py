##### PURPOSE: CREATION OF FORMS PAGE USED TO CREATE THE CLASS THAT WILL ULTIMATELY CONSIST OF OUR 'REGISTER' VIEW URL
# VERSION: 1.0
# DATE: 10.3.21
# VERSION MILESTONE: CREATE FORMS PAGE WHICH WILL BE USED TO BUILD OUT THE FHCALCULATOR

from django import forms
from django.contrib.auth.models import User
from .models import PedigreeQuestion, PedigreeChoice

# STEP 1 - CREATION OF THE REGISTERFORM() CLASS, WHICH IS INSTANTIATED BY THE USERCREATIONFORM DJANGO CLASS
class PedigreeForm(PedigreeQuestion):
    email = forms.EmailField()
    pedigreenumber = PedigreeChoice.choice_number
    name = forms.CharField(label = "Selection"
                           , max_length = 200)
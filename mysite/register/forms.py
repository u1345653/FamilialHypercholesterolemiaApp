##### PURPOSE: CREATION OF FORMS PAGE USED TO CREATE THE CLASS THAT WILL ULTIMATELY CONSIST OF OUR 'REGISTER' VIEW URL
# VERSION: 1.0
# DATE: 10.1.21
# VERSION MILESTONE: CREATE LOGIN PAGE WITH 4 FIELDS, ALL INCLUDED IN OUR DATA MODEL

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

# STEP 1 - CREATION OF THE REGISTERFORM() CLASS, WHICH IS INSTANTIATED BY THE USERCREATIONFORM DJANGO CLASS
class RegisterForm(UserCreationForm):
    email = forms.EmailField()                                   # DEFINING PREDETERMINED 'EMAIL' FIELD

    class Meta:                                                  # CREATION OF META CLASS WHICH DEFINES & ORDERS
        model = User                                               # THE FIELDS USERS WILL FILL OUT
        fields = ["username", "email", "password1", "password2"]
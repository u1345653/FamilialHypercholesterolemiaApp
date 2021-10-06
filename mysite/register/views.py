##### PURPOSE: CREATION OF REGISTRATION VIEW THAT WILL ALLOW USERS TO INPUT 4 VARIABLES TO CREATE A PROFILE
# VERSION: 1.0
# DATE - 10.1.21
# VERSION MILESTONE: CREATE LOGIN PAGE WITH 4 FIELDS, ALL INCLUDED IN OUR DATA MODEL

from django.shortcuts import render, redirect
from .forms import RegisterForm

# CREATING A FUNCTION THAT ENABLES THE USER TO VIEW THE WEBPAGE THEY VIEW IN ON; INSTANTIATED BY USERS RESPONSE
def register(response):
    if response.method == "POST":                   # CONDITIONAL STATEMENTS DETERMINING WHAT WE DO WITH
        form = RegisterForm(response.POST)          # THE USER INPUT IF THE METHOD IS 'POST'
        if form.is_valid():                              # WHAT WE DO WITH THE DATA IF THE INPUT IS 'VALID'
            form.save()                                            # SAVE THE USER INPUT DATA

        return redirect("/home")                                   # THEN REDIRECT THE USER TO OUR HOMEPAGE
    else:
        form = RegisterForm()                       # OTHERWISE, PROMPT THEM WITH THE REGISTRATION FORM CLASS

    return render(response, "register/register.html", {"form" : form})
from django.shortcuts import render, HttpResponse, redirect
from .forms import ExampleForm, PedigreeForm, InputForm

# Create your views here.
def fhcalc(request):
    if request.method == "POST":
        forma = PedigreeForm(request.POST)
        formb = InputForm(request.POST)


    else:
        forma = PedigreeForm()
        formb = InputForm()

    return render(request, "fhcalc/fhcalc.html", {
        'forma' : forma,
        'formb' : formb
    })
from django.shortcuts import render, redirect
# from .models import PedigreePerson, PersonInput
from django.urls import reverse
# from django.views import generic
from .forms import PedigreePerson, PersonInput, FormFilled
from django.http import HttpResponseRedirect


# Create your views here.
def index_view(request):
    template_name = 'fhcalc/index.html'

    if request.method == "POST":
        form = PersonInput(request.POST)
        if form.is_valid():
            age = form.cleaned_data["patient_age"]
            sex = form.cleaned_data["patient_sex"]
            dna_dx = form.clean_data["patient_dna_dx"]
            totc = form.cleaned_data["patient_totc"]
            ldlc = form.cleaned_data["patient_ldlc"]
            clincad_status = form.cleaned_data["patient_clincad_status"]
            clincad_age = form.cleaned_data["patient_clincad_age"]
            t = PersonInput(patient_age = age
                            , patient_sex = sex
                            , patient_dna_dx = dna_dx
                            , patient_totc = totc
                            , patient_ldlc = ldlc
                            , patient_clincad_status = clincad_status
                            , patient_clincad_age = clincad_age)
            t.save()
            return redirect(results_view(t.data), {'t':t})

    return render(request, template_name, {'forma': PedigreePerson, 'formb': PersonInput})

def results_view(request):
    print("HELLO GOVNA")
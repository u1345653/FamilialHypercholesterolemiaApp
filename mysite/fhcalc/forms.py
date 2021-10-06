from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

max_age = 110
patient_age = 0
AGE_CHOICES = [tuple([x,x]) for x in range(1, 110)]

MULTIPLE_OPTIONS = (
    (0, "Known and Undiagnosed"),
    (1, "Known and Confirmed Diagnosis"),
    (9, "Unkown")
    )

# TODO - RESEARCH HOW TO MAKE DJANGO FORMS CLASSES DYNAMIC -- AKA: HOW DO WE CREATE A NEW 'INPUT FORM' OBJECT, FOR EACH PEDIGREE FORM SELECTION?
class PedigreeForm(forms.Form):
    pedigree_selection = forms.TypedChoiceField(
        label = "Enter the Family-Pedigree being selected"
        , choices = (
            (0, "Grandmother on Parent #1 Side")
            , (1, "Grandfather on Parent #1 Side")
            , (3, "Sibling of Parent 1")
            , (4, "Sibling 2 of Parent 1")
            , (5, "Parent 1")
            , (2, "Parent 2")
            , (6, "Child of Parent 1 & Parent 2")
            , (7, "Child 2 of Parent 1 & Parent 2")
            , (8, "Child 3 of Parent 1 & Parent 2")
            )
        , coerce = lambda x:bool(int(x))
        , required = True
        )

class InputForm(forms.Form):
    patient_aqe = forms.TypedChoiceField(
        label = "Select Patients Age: ",
        coerce = lambda x:bool(int(x)),
        choices = AGE_CHOICES,
        required = False
    )

    patient_sex = forms.TypedChoiceField(
        label = "Select Patient Gender: ",
        choices = ((0, "Male"), (1, "Female")),
        coerce = lambda x:bool(int(x)),
        required = False
    )

    #TODO GET CLARITY ON WHAT OPTIONS SHOULD BE FOR 'DNA_DX' STATUS...? SAME AS TX & CAD..?
    patient_dna_dx = forms.TypedChoiceField(
        label = "Enter Patient DNA DX Status (if known):",
        choices = MULTIPLE_OPTIONS,
        required = False,
        initial = "DX Status"
    )


    patient_ldlc = forms.IntegerField(
        label = "Enter Patient LDL-C Level: ",
        initial = 0,
        required = False
    )


    patient_totc = forms.IntegerField(
        label = "Enter Patient TOT-C Level: ",
        initial = 0,
        required = False,
    )

    patient_tx = forms.TypedChoiceField(
        label = "Enter Patient TX Status (if Known): ",
        initial = 0,
        choices = MULTIPLE_OPTIONS,
        required = False,
    )

    patient_clincad_status = forms.TypedChoiceField(
        label = "Indicate if Patient has been Diagnosed with Coronary Artery Disease (CAD): ",
        initial = 0,
        choices = MULTIPLE_OPTIONS,
        required = False,
        )

    patient_clincad_age = forms.TypedChoiceField(
        label = "Enter Patients CAD Onset Age (if applicable): ",
        coerce = lambda x:bool(int(x)),
        choices = AGE_CHOICES,
        required = False
    )

class ExampleForm(forms.Form):
    like_website = forms.TypedChoiceField(
        label = "Do you like this website?",
        choices = ((1, "yes"), (0, "No")),
        coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '1',
        required = True,
    )

    favorite_food = forms.CharField(
        label = "What is your favorite food?",
        max_length=80,
        required = True,
    )

    favorite_color = forms.CharField(
        label = "What is your favorite Color?",
        max_length = 80,
        required = True,
    )

    favorite_number = forms.IntegerField(
        label = "Favorite Number",
        required = False,
    )

    notes = forms.CharField(
        label = "Additional Notes or Feedback?",
        required = False
    )


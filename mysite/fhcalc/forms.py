from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, ButtonHolder
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, Accordion, AccordionGroup
from django.forms import ChoiceField


class PedigreePerson(forms.Form):
    pub_date = forms.DateTimeField(label='Date Entered')

    person_choice = forms.ChoiceField(
        choices=(
            ('0', "Grandmother on Parent #1 Side")
            , ('1', "Grandfather on Parent #1 Side")
            , ('3', "Sibling of Parent 1")
            , ('4', "Sibling 2 of Parent 1")
            , ('5', "Parent 1")
            , ('2', "Parent 2")
            , ('6', "Child of Parent 1 & Parent 2")
            , ('7', "Child 2 of Parent 1 & Parent 2")
            , ('8', "Child 3 of Parent 1 & Parent 2"))
        , label='Pedigree Selection')

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.form_method = 'post'
    helper.form_id = 'pedigreechoice'
    helper.form_tag = False
    helper.layout = Layout(
        Field('person_choice', css_class='input-xlarge'), )


class PersonInput(forms.Form):
    max_age = 110
    AGE_CHOICES = [tuple([x, x]) for x in range(1, 110)]
    MULTIPLE_OPTIONS = (
        (0, "Known and Undiagnosed"),
        (1, "Known and Confirmed Diagnosis"),
        (9, "Unkown"))

    patient_age = forms.IntegerField(label="Age: ", max_value=max_age)
    patient_sex: ChoiceField = forms.ChoiceField(
        choices=(
            ('0', "Male")
            , ('1', "Female"))
        , label="Sex: ")

    patient_dna_dx = forms.ChoiceField(
        choices=MULTIPLE_OPTIONS,
        label="DNA DX Status: ")

    patient_ldlc = forms.IntegerField(label="LDL-C Level: ", required=False)

    patient_totc = forms.IntegerField(label="TOT-C Level: ", required=False)

    patient_tx = forms.ChoiceField(
        choices=MULTIPLE_OPTIONS,
        label="Patient TX: ")

    patient_clincad_status = forms.ChoiceField(
        choices=MULTIPLE_OPTIONS,
        label="Clinical CAD Status: ")

    patient_clincad_age = forms.IntegerField(label="Clinical CAD Onset Age: ", required=False)

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.form_id = 'person_input'
    helper.form_method = 'post'
    helper.form_tag = False
    helper.form_action = 'submit'
    helper.layout = Layout(
        Field(Div('patient_age'), css_class='input-xlarge'),
        Field('patient_sex', css_class='input-xlarge'),
        Field('patient_dna_dx', css_class='input-xlarge'),
        Field('patient_ldlc', css_class='input-xlarge'),
        Field('patient_totc', css_class='input-xlarge'),
        Field('patient_tx', css_class='input-xlarge'),
        Field('patient_clincad_status', css_class='input-xlarge'),
        Field('patient_clincad_age', css_class='input-xlarge'),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='btn-success'), ),
    )


class FormFilled(PersonInput):

    def __init__(self):
        super().__init__()
        age = self.patient_age
        ldlc = self.patient_ldlc
        totc = self.patient_totc
        tx_status = self.patient_tx
        clincad_status = self.patient_clincad_status
        clincad_age = self.patient_clincad_age
        sex = self.patient_sex

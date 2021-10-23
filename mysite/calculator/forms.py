from django.forms import Form, forms, IntegerField, ChoiceField

class Numberinput(forms.Form):
    num1 = IntegerField(
        label = 'Enter First Number', required = False
    )
    num2 = IntegerField(
        label = 'Enter Second Number', required = False
    )
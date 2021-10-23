from django.shortcuts import render
from .forms import Numberinput

# Create your views here.
def index(request):
    form = Numberinput()
    return render(request, 'input.html', {'form':form})

def addition(request):

    # num1b = Numberinput.cleaned_data['num1']
    # num2b = Numberinput.cleaned_data['num2']
    num1 = request.POST['num1']
    num2 = request.POST['num2']

    if num1.isdigit() and num2.isdigit():
        a = int(num1)
        b = int(num2)
        res = a + b

        return render(request, "result.html", {"result":res})

    # elif num1b.isdigit() and num2b.isdigit():
    #     a = int(num1b)
    #     b = int(num2b)
    #     res = a + b
    #
    #     return render(request, "result.html", {"result":res})
    else:
        res = "Only digits are allowed"
        return(request, "result.html", {"result":res})

def subtraction(request):

    num1 = request.POST['num1']
    num2 = request.POST['num2']

    if num1.isdigit() and num2.isdigit():
        a = int(num1)
        b = int(num2)
        res = a - b

        return render(request, "result.html", {"result":res})
    else:
        res = "Only digits are allowed"
        return render(request, "result.html", {"result":res})

def multiplication(request):

    num1 = request.POST['num1']
    num2 = request.POST['num2']

    if num1.isdigit() and num2.isdigit():
        a = int(num1)
        b = int(num2)
        res = a * b

        return render(request, "result.html", {"result":res})
    else:
        res = "Only digits are allowed"
        return render(request, "result.html", {"result":res})

def division(request):

    num1 = request.POST['num1']
    num2 = request.POST['num2']
    
    if num1.isdigit() and num2.isdigit():
        a = int(num1)
        b = int(num2)

        if b == 0:
            res = "Zero Divide Error"
            return render(request, "result.html", {"result":res})
        else:
            res = a / b
            return render(request, "result.html", {"result":res})
    else:
        res = "Only digits are allowed"
        return render(request, "result.html", {"result":res})
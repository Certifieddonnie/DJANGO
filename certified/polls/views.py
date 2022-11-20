from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def blah(request):
    return HttpResponse("Hello Blah!")


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html', {'name': 'McDonald', 'age': '18'})


def home2(request):
    return render(request, 'home2.html', {'name': 'McDonald', 'age': '18'})


def checker(request):
    return render(request, 'checker.html')


def add(request):

    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 + val2
    return render(request, 'result.html', {'result': res})


def sub(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 - val2
    return render(request, 'result.html', {'result': res})

# To determine operation to work on.


def check(request):
    oper = request.POST["ops"]

    oper = oper.lower()
    if oper == "add":
        return home(request)
    elif oper == "sub":
        return home2(request)
    else:
        return render(request, 'error.html')

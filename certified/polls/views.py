from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello, World! This is the polls index.")


def home(request):
    return render(request, 'home.html', {'name': 'McDonald', 'age': '18'})

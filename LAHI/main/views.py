from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request, 'main/homepage.html')
def loginS(request):
    return render(request, 'login.html')    
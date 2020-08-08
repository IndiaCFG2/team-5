from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
<<<<<<< HEAD
    return render(request, 'main/homepage.html')    
=======
    return render(request, 'main\homepage.html')
def loginS(request):
    return render(request, 'login.html')    
>>>>>>> 573eda1abcbf58a500a0da2be3195105e79b96d6

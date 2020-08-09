from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
from .forms import StudentAuthenticationForm
from django.contrib.auth.models import User
from teachers.models import Student
from main.models import MediaFile


def student_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # if 'next' in request.POST:
            return redirect('students:dashboard')
            # else:
                # return redirect('articles:list')
                
    else:
        form = AuthenticationForm()
    return render(request, 'students/login.html', { 'form': form })
    # return HttpResponse("Student login")

def materials(request):
    media = MediaFile.objects.all()
    return render(request, 'students/test.html', {'media':media})

def dashboard(request):
    return render(request, 'students/dashboard.html')

def agenda(request):
    return render(request, 'students/agenda.html')

def feedback(request):
    return render(request, 'students/feedback.html')    
 
def content(request):
    return render(request, 'students/feedback.html') 
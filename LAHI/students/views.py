from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
from .forms import StudentAuthenticationForm
from django.contrib.auth.models import User
from teachers.models import Student


def student_login(request):
    pass
    # if request.method == 'POST':
    #     form = StudentAuthenticationForm(data=request.POST)
    #     if form.is_valid():
    #         user = form['name']
    #         login(request, user)
    #         if 'next' in request.POST:
    #             return redirect(request.POST.get('next'))
    #         else:
                # return redirect('articles:list')
    #             return HttpResponse('You are logged in')
    # else:
    #     form = StudentAuthenticationForm()
    # return render(request, 'students/login.html', { 'form': form })
    # return HttpResponse("Student login")

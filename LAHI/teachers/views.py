from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
from .forms import *
from main.models import MediaFile, Standard

def teacher_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # if 'next' in request.POST:
            #     return redirect(request.POST.get('next'))
            # else:
            return redirect('teachers:dashboard')
                
    else:
        form = AuthenticationForm()
    return render(request, 'teachers/login.html', { 'form': form })
    # return HttpResponse("teacher login")

def upload_files(request):
    if request.method == 'POST':
        form = MediaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('File uploaded successfuly')
    else:
        form = MediaForm()
    return render(request, 'teachers/uploadfiles.html', {'form':form})

def materials(request):
    media = MediaFile.objects.all()
    return render(request, 'teachers/content.html', {'media':media})

def create_student(request):
    # return HttpResponse("hello there")
    if request.method == 'POST':
        if request.POST['pass'] == request.POST['passagain']:
            try:
                user = User.objects.get(username=request.POST['uname'])
                roll_no = Student.objects.get(roll_no=request.POST['roll_no'])
                return render(request, 'teachers/createstudent.html', {'error':"User already exist!"})
            except User.DoesNotExist or Student.DoesNotExist:
                roll_no = request.POST['rollno']
                phone = request.POST['phone']
                std = Standard.objects.get(standard=request.POST['std'])
                user = User.objects.create_user(username=request.POST['uname'], password=request.POST['pass'])
                student = Student(user=user, roll_no=roll_no, phone=phone, std=std)
                student.save()
                return HttpResponse("user created")
        else:
            return render(request, 'teachers/createstudent.html', {'error':"Password doesn't match"})
    
    return render(request, 'teachers/createstudent.html')
        # return HttpResponse("create a new user")

def dashboard(request):
    return render(request, 'teachers/dashboard.html')

def agenda(request):
    return render(request, 'teachers/agenda.html')
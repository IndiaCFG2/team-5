from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
from .forms import *
from main.models import MediaFile

def teacher_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                # return redirect('articles:list')
                return HttpResponse('You are logged in')
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
    if request.method == 'POST':
        if request.POST['pass'] == request.POST['passagain']:
            try:
                user = User.objects.get(username=request.POST['uname'])
                roll_no = Student.objects.get(roll_no=request.POST['roll_no'])
                return render(request, 'teachers/createstudent.html', {'error':"User already exist!"})
            except:
                roll_no = request.POST['rollno']
                phone = request.POST['phone']
                user = User.objects.create_user(username=request.POST['uname'], password=request.POST['pass'])
                student = Student(user=user, roll_no=roll_no, phone=phone)
                return HttpResponse("user created")
        else:
            return render(request, 'teachers/createstudent.html', {'error':"Password doesn't match"})
    else:
        render(request, 'teacher/createstudent.html')




    # if request.method == 'POST':
    #     form = NewStudentForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponse('Student created')
    # else:
    #     form = NewStudentForm()
    # return render(request, 'teachers/createstudent.html', {'form':form})

    


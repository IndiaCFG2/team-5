from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse

def student_login(request):
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
    return render(request, 'students/login.html', { 'form': form })
    # return HttpResponse("Student login")
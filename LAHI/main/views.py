from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MediaFile
import mimetypes
from django.contrib.auth import logout

# Create your views here.
def homepage(request):
    return render(request, 'main/homepage.html')  

def download(request, filename):
    fl_path = 'media/'
    print(filename)
    filename = filename
    fl = open(fl_path+filename, 'rb')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

def logout_view(request):
    if request.method == 'POST':
	    logout(request)
	    return redirect('main:homepage')


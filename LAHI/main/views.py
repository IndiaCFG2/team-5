from django.shortcuts import render
from django.http import HttpResponse
from .models import MediaFile
import mimetypes

# Create your views here.
def homepage(request):
    return render(request, 'main/homepage.html')  

def download(request, filename):
    fl_path = '/media/'
    filename = filename
    fl = open(fl_path, 'r')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response


from django.shortcuts import redirect, render
import mimetypes
from django.http import HttpResponse
from wsgiref.util import FileWrapper
import os
from .models import *

# Create your views here.
def home(request):
    file=down.objects.get(pk=1)
    return render(request, 'index.html',{'down':down})




def download_file(request):
    # fill these variables with real values
    fl_path = '/media/KARTIKEY_KAKRAN CV.pdf'
    filename = 'KARTIKEY_KAKRAN CV.pdf'

    fl = open(fl_path, 'r')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type='application/pdf')
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
    
# def download_pdf(request):
#     filename = 'KARTIKEY_KAKRAN CV.pdf'
#     content = FileWrapper(filename)
#     response = HttpResponse(content, content_type='application/pdf')
#     response['Content-Length'] = os.path.getsize(filename)
#     response['Content-Disposition'] = 'attachment; filename=%s' % 'KARTIKEY_KAKRAN CV.pdf'
#     return response
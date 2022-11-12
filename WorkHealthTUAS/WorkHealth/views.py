from django.shortcuts import render

from .models import Survey

# Create your views here.

def index(request):
    #The home page
    return render(request, 'WorkHealth/index.html')

def surveys(request):
    #Show that week's survey
    surveys = Survey.objects
    context = {'surveys':surveys}
    return render(request, 'WorkHealth/index.html', context)
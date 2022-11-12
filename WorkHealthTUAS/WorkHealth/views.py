from django.shortcuts import render

from .models import Survey

# Create your views here.

def index(request):
    #The home page
    return render(request, 'WorkHealth/index.html')

def surveys(request):
    #Show that week's survey, Not sure if this works
    surveys = Survey.objects.order_by('date_added')
    survey = surveys[0]
    context = {'surveys':survey}
    return render(request, 'WorkHealth/index.html', context)
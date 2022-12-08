from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.detail import DetailView
from .models import Survey, Question, Admin, UserAnswer, Option, Result

# Create your views here.

def index(request):
    question = Question.objects
    option = Option.objects.all()
    context = {"questions": question, "options": option}

    return render(request, 'WorkHealth/index.html', context)

def index2(request):
    question = Question.objects
    option = Option.objects.all()
    context = {"questions": question, "options": option}

    return render(request, 'WorkHealth/index2.html', context)

def thankyou(request):
    return render(request, 'WorkHealth/thankyou.html')

def piechart(request):
    return render(request, 'WorkHealth/week40.html')

# class survey(DetailView):
#     model = Survey
#     def get_context_data(self, **kwargs):
#         context = super(survey, self).get_context_data(**kwargs)
#         return super().get_context_data(**kwargs)

def survey(request, survey_id):
    survey = Survey.objects.get(pk=survey_id)
    context = {'survey': survey}
    return render(request, 'WorkHealth/survey.html', context)

def result(request):
    # Show list of surveys
    surveys = Survey.objects.all()
    context = {'surveys': surveys}
    return render(request, 'WorkHealth/results.html', context)
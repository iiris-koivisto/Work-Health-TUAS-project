"""Defines URL patterns for WorkHealth."""
from django.urls import path
from . import views

app_name = 'WorkHealth'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('index2/', views.index, name='index2'),
    #path('survey/<survey_id>/', views.survey, name='survey')
    path('results/', views.result, name='results'),
]
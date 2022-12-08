"""Defines URL patterns for WorkHealth."""
from django.urls import path
from . import views

app_name = 'WorkHealth'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('index2/', views.index2, name='index2'),
    path('thankyou/', views.thankyou, name='thankyou'),
    #path('survey/<survey_id>/', views.survey, name='survey')
    path('results/', views.result, name='results'),
    path('results/week40/', views.piechart, name='week40'),
]
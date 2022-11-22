"""Defines URL patterns for WorkHealth."""
from django.urls import path
from . import views

app_name = 'WorkHealth'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]
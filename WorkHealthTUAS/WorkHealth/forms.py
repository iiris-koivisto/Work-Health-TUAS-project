from django import forms

from .models import Survey

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['text']
        labels = {'text': 'Write your answer here'}
        
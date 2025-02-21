# lms_app/forms.py
from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

from .models import Course, Assignment

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description']
        labels = {
            'title': 'Название курса',
            'description': 'Описание курса',
        }

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'description']
        labels = {
            'title': 'Название задания',
            'description': 'Описание задания',
        }


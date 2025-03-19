from django.shortcuts import render
from django.views import generic
from .models import Exercise

# Create your views here.
class ExerciseList(generic.ListView):
    queryset = Exercise.objects.all()
    template_name = "exercise_list.html"
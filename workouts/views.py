from django.shortcuts import render
from django.views import generic
from .models import Exercise

# Create your views here.
class ExerciseList(generic.ListView):
    model = Exercise
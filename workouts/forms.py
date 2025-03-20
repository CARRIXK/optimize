from django import forms
from .models import Workout, Exercise, ExerciseSet

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['title']

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'description']

class ExerciseSetForm(forms.ModelForm):
    class Meta:
        model = ExerciseSet
        fields = ['set_number', 'reps', 'weight']


from django import forms
from .models import Workout, Exercise, ExerciseType, ExerciseSet

# Form for creating and updating workouts
class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['title']

# Form for creating and updating exercises
class ExerciseForm(forms.ModelForm):
    workout = forms.ModelChoiceField(queryset=Workout.objects.all(), empty_label="Select a Workout")
    exercise_type = forms.ModelChoiceField(queryset=ExerciseType.objects.all(), empty_label="Select an Exercise Type")
    
    class Meta:
        model = Exercise
        fields = ['workout', 'exercise_type']

# Form for creating and updating exercise sets
class ExerciseSetForm(forms.ModelForm):
    exercise = forms.ModelChoiceField(queryset=Exercise.objects.all(), empty_label="Select an Exercise")
    
    class Meta:
        model = ExerciseSet
        fields = ['exercise', 'set_number', 'reps', 'weight']
from django import forms
from .models import Workout, Exercise, Set, ExerciseSet

# Form for creating and updating workouts
class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['title']

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['workout', 'exercise_type', 'sets_reps']


class SetForm(forms.ModelForm):
    class Meta:
        model = Set
        fields = ['exercise', 'sets']



# Form for creating and updating exercise sets
class ExerciseSetForm(forms.ModelForm):
    exercise = forms.ModelChoiceField(queryset=Exercise.objects.all(), empty_label="Select an Exercise")
    
    class Meta:
        model = ExerciseSet
        fields = ['exercise', 'set_number', 'reps', 'weight']
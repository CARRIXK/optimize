from django.db import models
from django.contrib.auth.models import User



class ExerciseType(models.Model):
    exercise_name = models.CharField(max_length=200, unique=True, default="Default Exercise Name")
    description_url = models.URLField(blank=True, null=True, default="https://example.com")
    exercise_image = models.URLField(blank=True, null=True, default="https://example.com/image.jpg")
    exercise_image1 = models.URLField(blank=True, null=True, default="https://example.com/image1.jpg")
    muscle_group_details = models.URLField(blank=True, null=True, default="https://example.com/muscle-group")
    muscle_group = models.CharField(max_length=100, default="Generic Muscle Group")
    equipment_details = models.URLField(blank=True, null=True, default="https://example.com/equipment")
    equipment = models.CharField(max_length=100, default="Generic Equipment")
    rating = models.FloatField(blank=True, null=True, default=5.0)  # Assuming a default rating of 5
    description = models.CharField(max_length=255, blank=True, null=True, default="No description provided")

    def __str__(self):
        return self.exercise_name
    

class Workout(models.Model):
    title = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Exercise(models.Model):
    workout = models.ForeignKey(Workout, related_name='exercises', on_delete=models.CASCADE, null=True, blank=True) 
    exercise_type = models.ForeignKey('ExerciseType', related_name='exercises', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Exercise {self.exercise_type.name if self.exercise_type else 'Unnamed'}"


class ExerciseLog(models.Model):
    workout_session = models.ForeignKey('WorkoutSession', on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, null=True, blank=True)
    sets = models.IntegerField()
    reps = models.IntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.exercise.exercise_type.name if self.exercise and self.exercise.exercise_type else 'Unnamed'} - {self.sets} sets of {self.reps} reps"
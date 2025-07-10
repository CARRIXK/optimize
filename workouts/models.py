from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.contrib.postgres.fields import ArrayField



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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Exercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name="exercises", null=True)
    exercise_type = models.ForeignKey(ExerciseType, on_delete=models.CASCADE, related_name="exercises", null=True)

    

class Set(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="sets")
    set_number = models.PositiveIntegerField(null=True, blank=True)  # Allow nulls for migration ease
    reps = models.PositiveIntegerField(null=True, blank=True)  # Allow reps to be null
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Optional weight

    def __str__(self):
        return f"{self.exercise.exercise_type.exercise_name} - {self.reps} reps"



class ExerciseSet(models.Model):
    exercise = models.ForeignKey(Exercise, related_name='excercise_sets', on_delete=models.CASCADE, null=True, blank=True)
    set_number = models.IntegerField()
    reps = models.IntegerField()
    weight = models.FloatField()

    def __str__(self):
        return f"Set {self.set_number} - {self.reps} reps"


class WorkoutSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    exercises = models.ManyToManyField(Exercise, through='ExerciseLog')
    total_duration = models.IntegerField()
    date_completed = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_completed"]

    def __str__(self):
        return f"Workout: {self.title} completed by {self.user}"


class ExerciseLog(models.Model):
    workout_session = models.ForeignKey(WorkoutSession, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, null=True, blank=True)
    sets = models.IntegerField()
    reps = models.IntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.exercise.exercise_type.name if self.exercise and self.exercise.exercise_type else 'Unnamed'} - {self.sets} sets of {self.reps} reps"
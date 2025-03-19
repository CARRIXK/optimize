from django.db import models
from django.contrib.auth.models import User



class Exercise(models.Model):
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
    
    
class WorkoutSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link workout to a specific user
    title = models.CharField(max_length=200)  # Title for the workout session
    date = models.DateField(auto_now_add=True)  # Automatically set to current date
    exercises = models.ManyToManyField(Exercise, through='ExerciseLog')  # Many to Many with Exercise, through a join model
    total_duration = models.IntegerField()  # Duration of the workout in minutes
    date_completed = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["-date_completed"]
    
    def __str__(self):
        return f"Workout: {self.title} completed by {self.user}"
    


class ExerciseLog(models.Model):
    workout_session = models.ForeignKey(WorkoutSession, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.IntegerField()
    reps = models.IntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)  # Weight lifted (kg or lbs)
    
    def __str__(self):
        return f"{self.exercise.name} - {self.sets} sets of {self.reps} reps"
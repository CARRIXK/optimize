from django.contrib import admin
from .models import Exercise, WorkoutSession, ExerciseLog

# Register your models here.
admin.site.register(Exercise)
admin.site.register(WorkoutSession)
admin.site.register(ExerciseLog)
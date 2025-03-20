from django.contrib import admin
from .models import ExerciseType, Workout, WorkoutSession, ExerciseLog
from django_summernote.admin import SummernoteModelAdmin


@admin.register(ExerciseType)
class ExerciseAdmin(SummernoteModelAdmin):
    list_display = ('exercise_name', 'muscle_group', 'equipment', 'rating')
    search_fields = ['exercise_name', 'muscle_group', 'equipment']
    summernote_fields = ('description',)

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['title']

# Register your models here.
# admin.site.register(Exercise)
admin.site.register(WorkoutSession)
admin.site.register(ExerciseLog)
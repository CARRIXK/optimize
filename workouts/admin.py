from django.contrib import admin
from .models import Exercise, WorkoutSession, ExerciseLog
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Exercise)
class ExerciseAdmin(SummernoteModelAdmin):
    list_display = ('exercise_name', 'muscle_group', 'equipment', 'rating')
    search_fields = ['exercise_name', 'muscle_group', 'equipment']
    summernote_fields = ('description',)


# Register your models here.
# admin.site.register(Exercise)
admin.site.register(WorkoutSession)
admin.site.register(ExerciseLog)
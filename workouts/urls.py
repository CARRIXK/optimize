from . import views
from django.urls import path

urlpatterns = [
    path('create/', views.create_workout, name='create_workout'),
    path('add_exercises', views.add_exercises, name='add_exercises'),
    path('add_exercise_sets/<int:exercise_id>/', views.add_exercise_sets, name='add_exercise_sets'),
    path('excersises', views.ExerciseList.as_view(), name='Exercise-List'),
    path('import/', views.import_excel_data, name='import_excel_data'),
    path('', views.workout_list, name='workouts'),
]
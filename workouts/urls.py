from . import views
from django.urls import path

urlpatterns = [
    path('create/', views.create_workout, name='create_workout'),
    path('add_exercises', views.add_exercises, name='add_exercises'),
    path('add_exercise_sets', views.add_exercise_sets, name='add_exercise_sets'),
    path('save_workout', views.save_workout, name='save_workout'),
    path('add_exercise_sets/<int:exercise_id>/', views.add_exercise_sets, name='add_exercise_sets'),
    path('excersises', views.ExerciseList.as_view(), name='Exercise-List'),
    path('delete_workout/<int:id>/', views.delete_workout, name='delete_workout'),  # URL pattern for delete_workout
    path('edit_workout/<int:id>/', views.edit_workout, name='edit_workout'),  # URL pattern for edit_workout
    path('update_workout/', views.update_workout, name='update_workout'),  # URL pattern for delete_workout
    path('import/', views.import_excel_data, name='import_excel_data'),
    path('', views.workout_list, name='workouts'),
]
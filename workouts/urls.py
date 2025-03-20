from . import views
from django.urls import path

urlpatterns = [
    path('excersises', views.ExerciseList.as_view(), name='Exercise-List'),
    path('import/', views.import_excel_data, name='import_excel_data'),
    path('', views.workout_list, name='workouts'),
]
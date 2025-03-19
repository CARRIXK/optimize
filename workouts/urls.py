from . import views
from django.urls import path

urlpatterns = [
    path('', views.ExerciseList.as_view(), name='Exercise-List'),
]
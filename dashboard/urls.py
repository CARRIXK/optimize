from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    # path('workouts/create/', views.create_workout, name='create_workout'),
]
from django.db import models
from django.contrib.auth.models import User


class Exercise(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description_url = models.URLField(blank=True, null=True)
    exercise_image = models.URLField(blank=True, null=True)
    exercise_image1 = models.URLField(blank=True, null=True)
    muscle_group_details = models.TextField(blank=True, null=True)
    muscle_group = models.CharField(max_length=100)
    equipment_details = models.TextField(blank=True, null=True)
    equipment = models.CharField(max_length=100)
    rating = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name
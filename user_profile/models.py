from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    birth_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], blank=True)
    units_of_measure = models.CharField(max_length=10, choices=[('Metric', 'Metric'), ('Imperial', 'Imperial')], default='Metric')
    weight = models.FloatField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

# Generated by Django 4.2.20 on 2025-03-20 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0009_exercisetype_remove_exercise_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='exercise_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='workouts.exercisetype'),
        ),
    ]

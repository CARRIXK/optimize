# Generated by Django 4.2.20 on 2025-03-19 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0006_rename_description_exercise_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise',
            old_name='muscle_gp',
            new_name='muscle_group',
        ),
        migrations.RenameField(
            model_name='exercise',
            old_name='muscle_gp_details',
            new_name='muscle_group_details',
        ),
    ]

# Generated by Django 4.2.20 on 2025-03-20 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0012_alter_exercise_workout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 4.2.20 on 2025-03-19 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0003_alter_workoutsession_options_exercise_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='muscle_group',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='muscle_group_details',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='name',
        ),
        migrations.AddField(
            model_name='exercise',
            name='exercise_name',
            field=models.CharField(default='Default Exercise Name', max_length=200, unique=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='muscle_gp',
            field=models.CharField(default='Generic Muscle Group', max_length=100),
        ),
        migrations.AddField(
            model_name='exercise',
            name='muscle_gp_details',
            field=models.URLField(blank=True, default='https://example.com/muscle-group', null=True),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='description',
            field=models.CharField(blank=True, default='No description provided', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='description_url',
            field=models.URLField(blank=True, default='https://example.com', null=True),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='equipment',
            field=models.CharField(default='Generic Equipment', max_length=100),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='equipment_details',
            field=models.URLField(blank=True, default='https://example.com/equipment', null=True),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='exercise_image',
            field=models.URLField(blank=True, default='https://example.com/image.jpg', null=True),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='exercise_image1',
            field=models.URLField(blank=True, default='https://example.com/image1.jpg', null=True),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='rating',
            field=models.FloatField(blank=True, default=5.0, null=True),
        ),
    ]

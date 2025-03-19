# Generated by Django 4.2.20 on 2025-03-19 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description_url', models.URLField(blank=True, null=True)),
                ('exercise_image', models.URLField(blank=True, null=True)),
                ('exercise_image1', models.URLField(blank=True, null=True)),
                ('muscle_group_details', models.TextField(blank=True, null=True)),
                ('muscle_group', models.CharField(max_length=100)),
                ('equipment_details', models.TextField(blank=True, null=True)),
                ('equipment', models.CharField(max_length=100)),
                ('rating', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]

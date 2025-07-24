from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Workout, ExerciseType, Exercise, Set

class WorkoutModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.workout = Workout.objects.create(title='Test Workout', user=self.user)

    def test_workout_str(self):
        self.assertEqual(str(self.workout), 'Test Workout')

class ExerciseTypeModelTest(TestCase):
    def test_exercise_type_str(self):
        et = ExerciseType.objects.create(exercise_name='Push Up')
        self.assertEqual(str(et), 'Push Up')

class ExerciseModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.workout = Workout.objects.create(title='Test Workout', user=self.user)
        self.exercise_type = ExerciseType.objects.create(exercise_name='Push Up')
        self.exercise = Exercise.objects.create(workout=self.workout, exercise_type=self.exercise_type)

    def test_exercise_str(self):
        self.assertIn('Push Up', str(self.exercise))

class SetModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.workout = Workout.objects.create(title='Test Workout', user=self.user)
        self.exercise_type = ExerciseType.objects.create(exercise_name='Push Up')
        self.exercise = Exercise.objects.create(workout=self.workout, exercise_type=self.exercise_type)
        self.set = Set.objects.create(exercise=self.exercise, set_number=1, reps=10)

    def test_set_str(self):
        self.assertIn('Set 1', str(self.set))

class WorkoutViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.workout = Workout.objects.create(title='Test Workout', user=self.user)

    def test_workout_list_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('workout_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Workout')

    def test_create_workout_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('create_workout'))
        self.assertEqual(response.status_code, 200)

    def test_delete_workout_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('delete_workout', args=[self.workout.id]))
        self.assertRedirects(response, reverse('workout_list'))
        self.assertFalse(Workout.objects.filter(id=self.workout.id).exists())

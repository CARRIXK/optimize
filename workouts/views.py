from django.shortcuts import render, redirect
from django.views import generic
from .models import Exercise, Workout, ExerciseType
from .forms import WorkoutForm, ExerciseForm, ExerciseSetForm

# Create your views here.
class ExerciseList(generic.ListView):
    queryset = ExerciseType.objects.all()
    template_name = "excersise_list.html"
    paginate_by = 2

def workout_list(request):
    workouts = Workout.objects.all()
    return render(request, 'workouts/workout_list.html', {'workouts': workouts})


# Create a new workout
def create_workout(request):
    return render(request, 'workouts/create_workout.html')


# Add exercises to a workout
def add_exercises(request):
    workout_title = None
    exercises = ExerciseType.objects.all()  # Retrieves all exercise types

    if request.method == 'POST':
        workout_title = request.POST.get('workout_title')  # Get workout title from the form data
    
    return render(request, 'workouts/add_exercises.html', {
        'workout_title': workout_title,
        'exercises': exercises
    })


# Add sets to an exercise
def add_exercise_sets(request, exercise_id):
    exercise = Exercise.objects.get(id=exercise_id)

    if request.method == 'POST' and 'create_set' in request.POST:
        exercise_set_form = ExerciseSetForm(request.POST)
        if exercise_set_form.is_valid():
            exercise_set = exercise_set_form.save(commit=False)
            exercise_set.exercise = exercise
            exercise_set.save()
            return redirect('add_exercise_sets', exercise_id=exercise.id)
    else:
        exercise_set_form = ExerciseSetForm()

    return render(request, 'workouts/add_exercise_sets.html', {
        'exercise_set_form': exercise_set_form,
        'exercise': exercise
    })




import openpyxl
from django.shortcuts import render
from .models import Exercise

# def import_excel_data(request):
#     if request.method == "POST" and request.FILES["file"]:
#         # Get the uploaded file
#         file = request.FILES["file"]
#         wb = openpyxl.load_workbook(file)
#         sheet = wb.active

#         for row in sheet.iter_rows(min_row=2, values_only=True):
#             exercise_name, description_url, exercise_image, exercise_image1, muscle_group_details, muscle_group, equipment_details, equipment,  rating , description = row

#             # Create the Exercise objects
#             Exercise.objects.create(
#                 exercise_name=exercise_name,
#                 description_url=description_url,
#                 exercise_image=exercise_image,
#                 exercise_image1=exercise_image1,
#                 muscle_group_details=muscle_group_details,
#                 muscle_group=muscle_group,
#                 equipment_details=equipment_details,
#                 equipment=equipment,
#                 rating=rating,
#                 description=description
#             )
#         return render(request, 'workouts/success.html')  # A success page after import
#     return render(request, 'workouts/import_form.html')  # A form page where you upload the file

def import_excel_data(request):
    if request.method == "POST" and request.FILES["file"]:
        # Get the uploaded file
        file = request.FILES["file"]
        wb = openpyxl.load_workbook(file)
        sheet = wb.active

        for row in sheet.iter_rows(min_row=2, values_only=True):
            exercise_name, description_url, exercise_image, exercise_image1, muscle_group_details, muscle_group, equipment_details, equipment, rating, description = row

            # Check if the exercise already exists in the database
            if not ExerciseType.objects.filter(exercise_name=exercise_name).exists():
                # Create the Exercise objects if it does not exist
                ExerciseType.objects.create(
                    exercise_name=exercise_name,
                    description_url=description_url,
                    exercise_image=exercise_image,
                    exercise_image1=exercise_image1,
                    muscle_group_details=muscle_group_details,
                    muscle_group=muscle_group,
                    equipment_details=equipment_details,
                    equipment=equipment,
                    rating=rating,
                    description=description
                )
            else:
                # Log a message or handle the case when duplicate exercise is found
                print(f"Exercise '{exercise_name}' already exists and will be skipped.")

        return render(request, 'workouts/success.html')  # A success page after import
    return render(request, 'workouts/import_form.html')  # A form page where you upload the file




    

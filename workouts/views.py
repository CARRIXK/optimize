from django.shortcuts import render, redirect
from django.views import generic
from .models import Exercise, Workout
from .forms import WorkoutForm, ExerciseForm

# Create your views here.
class ExerciseList(generic.ListView):
    queryset = Exercise.objects.all()
    template_name = "excersise_list.html"
    paginate_by = 2

def workout_list(request):
    workouts = Workout.objects.all()
    return render(request, 'workouts/workout_list.html', {'workouts': workouts})


# View to create the workout title
def create_workout(request):
    if request.method == 'POST' and 'create_workout' in request.POST:
        workout_form = WorkoutForm(request.POST)
        if workout_form.is_valid():
            workout = workout_form.save()
            return redirect('add_exercises', workout_id=workout.id)
    else:
        workout_form = WorkoutForm()

    return render(request, 'workouts/create_workout.html', {'workout_form': workout_form})


# View to add exercises to a created workout
def add_exercises(request, workout_id):
    workout = Workout.objects.get(id=workout_id)
    if request.method == 'POST' and 'add_exercise' in request.POST:
        exercise_form = ExerciseForm(request.POST)
        if exercise_form.is_valid():
            exercise = exercise_form.save(commit=False)
            exercise.workout = workout
            exercise.save()
            return redirect('add_exercises', workout_id=workout.id)
    else:
        exercise_form = ExerciseForm()

    return render(request, 'workouts/add_exercises.html', {
        'exercise_form': exercise_form,
        'workout': workout
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
            if not Exercise.objects.filter(exercise_name=exercise_name).exists():
                # Create the Exercise objects if it does not exist
                Exercise.objects.create(
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




    

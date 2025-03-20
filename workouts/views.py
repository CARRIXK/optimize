from django.shortcuts import render, redirect
from django.views import generic
from .models import Exercise, Workout, ExerciseType
from .forms import WorkoutForm, ExerciseForm, ExerciseSetForm
import ast

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
    workout_title = request.GET.get('workout_title', '')  # Get workout_title from query parameters, default to an empty string if not provided
    if(workout_title):
        context = {
            'workout_title': workout_title,
        }
        return render(request, 'workouts/create_workout.html', context)
    return render(request, 'workouts/create_workout.html')



# Add exercises to a workout
def add_exercises(request):
    workout_title = None

    if request.method == 'POST':
        workout_title = request.POST.get('workout_title')  # Get workout title from the form data
    
    query = request.GET.get('q')
    if query:
        exercises = ExerciseType.objects.filter(exercise_name__icontains=query).exclude(exercise_image__isnull=True)
    else:
        exercises = ExerciseType.objects.exclude(exercise_image__isnull=True)
    
    context = {
        'exercises': exercises,
        'workout_title': workout_title,  # Replace with actual workout title
    }
    return render(request, 'workouts/add_exercises.html', context)


# Add sets to an exercise
def add_exercise_sets(request):
    if request.method == 'POST':
        workout_title = request.POST.get('workout_title')
        selected_excersises = request.POST.get('selected_excersises')
        
        # Convert the string of exercises into a list
        try:
            selected_excersises = ast.literal_eval(selected_excersises)
        except (ValueError, SyntaxError):
            selected_excersises = []  # Default to an empty list if conversion fails

        # Filter ExerciseType objects based on selected exercise names
        matching_exercises = ExerciseType.objects.filter(exercise_name__in=selected_excersises)

        
        context = {
            'selected_excersises': matching_exercises,
            'workout_title': workout_title,
        }
        return render(request, 'workouts/workout_set_reps.html', context)




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




    

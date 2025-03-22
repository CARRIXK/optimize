from django.shortcuts import render, redirect
from django.views import generic
from .models import Exercise, Workout, ExerciseType, Set
from .forms import WorkoutForm, ExerciseForm, SetForm, ExerciseSetForm
import ast
import json
from django.http import JsonResponse

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
    

    
def save_workout(request):
    if request.method == "POST":
        print("Data sent from front end: ", request.POST)
        
        # # Check if a workout with the same title already exists
        # if Workout.objects.filter(title=workout_title).exists():
        #     return JsonResponse({'status': 'error', 'message': 'Workout with this title already exists.'})
        
        # # Create and validate WorkoutForm
        # workout_form = WorkoutForm(request.POST)

        # if workout_form.is_valid():
        #     # Save the workout form data to the database
        #     workout = workout_form.save(commit=False)
        #     # You can do additional operations here if needed, such as adding related data
        #     # Example: workout.user = request.user  (if you have user-based data)

        #     workout.save()  # Save the workout to the database

        #     # Print a success message
        #     print('Workout saved successfully!')
        #     print('Workout ID:', workout.id)  # Optionally print the workout ID or other relevant info
        #     return JsonResponse({'status': 'success', 'message': 'Workout saved successfully!'})
        # else:
        #     # Print an error if the form is not valid
        #     print('Invalid form data. Please check your inputs.')
        #     return JsonResponse({'status': 'error', 'message': 'Invalid form data. Please check your inputs.'})
        

        title = request.POST.get('title')
        print("title")
        exercises_json = request.POST.get("exercise_type")  # This is a string
        print("Excercises Json: ",exercises_json)

        # Deserialize JSON string into Python list
        exercises = json.loads(exercises_json)  

        # Create Workout object
        workout = Workout.objects.create(title=title)

        # Process exercises and sets
        for exercise_data in exercises:
            #get or create excercise type instance
            exercise_type = ExerciseType.objects.get(exercise_name=exercise_data["exercise_type"])

            exercise = Exercise.objects.create(
                workout=workout,
                exercise_type=exercise_type 
            )
            print("This is the created excersise object", exercise.workout, exercise.exercise_type)
            for set_data in exercise_data["set_reps"]:
                set_obj = Set.objects.create(
                    exercise=exercise,
                    set_number=set_data["set"],
                    reps=set_data["reps"]
                )
                print(f"Set created: Exercise - {set_obj.exercise}, Set Number - {set_obj.set_number}, Reps - {set_obj.reps}")
                
        

        
        # for exercise_data in exercises_data:
        #     exercise_type_name = exercise_data['exercise_type']
        #     set_reps = exercise_data['set_reps']

        #     print("Exercise type name: ", exercise_type_name)
        #     print("Sets reps to be inserted", set_reps)

        #     # Create a new ExerciseForm instance with the exercise data
        #     exercise_form = ExerciseForm({
        #     'workout': workout_title,
        #     'exercise_type': exercise_type_name,
        #     'set_reps': set_reps,
        #     })

        #     if exercise_form.is_valid():
        #         # Save the exercise form data to the database
        #         exercise = exercise_form.save(commit=False)
        #         exercise.workout = workout_title  # Associate the exercise with the workout
        #         exercise.save()

        #         # Print a success message
        #         print('Exercise saved successfully!')
        #         print('Exercise ID:', exercise.id)  # Optionally print the exercise ID or other relevant info
        #     else:
        #         # Print an error if the form is not valid
        #         print('Invalid form data. Please check your inputs.')
        #         print('Form errors:', exercise_form.errors)
        #         return JsonResponse({'status': 'error', 'message': 'Invalid form data. Please check your inputs.', 'errors': exercise_form.errors})

        # return JsonResponse({'status': 'success', 'message': 'Workout saved successfully!'})
            

        

        # if exercise_form.is_valid():
        #     try:
        #         exercise = exercise_form.save(commit=False)
        #         exercise.workout = workout  # Associate the exercise with the workout
        #         exercise.save()
        #     except Exception as e:
        #         print(f'Error saving exercise: {e}')
        #         return JsonResponse({'status': 'error', 'message': f'Error saving exercise: {e}'})
        # else:
        #     print('Invalid exercise form data. Please check your inputs.')
        #     print('Form errors:', exercise_form.errors)
        #     return JsonResponse({'status': 'error', 'message': 'Invalid exercise form data. Please check your inputs.', 'errors': exercise_form.errors})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})



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




    

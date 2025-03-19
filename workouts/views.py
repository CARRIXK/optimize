from django.shortcuts import render
from django.views import generic
from .models import Exercise

# Create your views here.
class ExerciseList(generic.ListView):
    queryset = Exercise.objects.all()
    template_name = "excersise_list.html"
    paginate_by = 2

# Create your views here.
class Home(generic.ListView):
    queryset = Exercise.objects.all()
    template_name = "workouts/index.html"
    paginate_by = 6


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




    

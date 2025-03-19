from django.shortcuts import render

# # Create your views here.
def dashboard(request):
    # workouts = WorkoutSession.objects.filter(user=request.user).order_by('-date_completed')[:5]
    return render(request, 'dashboard/dashboard.html')
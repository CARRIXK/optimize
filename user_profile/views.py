from django.shortcuts import render
from .models import UserProfile

# Create your views here.
def user_profile(request):
    """
    Renders the user profile page for the logged-in user
    """
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.filter(user=request.user).first()
    else:
        user_profile = None

    return render(
        request,
        "user_profile/user_profile.html",
        {"user_profile": user_profile},
    )
from django.contrib import admin
from .models import UserProfile
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(SummernoteModelAdmin):

    summernote_fields = ('bio',)


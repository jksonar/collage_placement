from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, StudentProfile

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'user_type']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['course', 'branch', 'section', 'cgpa']
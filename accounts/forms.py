from django import forms
from .models import StudentProfile,User
from django.contrib.auth.forms import UserCreationForm

class StudentUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model=StudentProfile
        fields=['student_id','course','year','guardian_name','guardian_phone','address']

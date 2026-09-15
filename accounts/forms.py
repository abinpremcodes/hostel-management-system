from django import forms
from .models import StudentProfile

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model=StudentProfile
        fields=['user','student_id','course','year','guardian_name','guardian_phone','address']

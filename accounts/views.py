from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import StudentProfile

@login_required

def student_list(request):
    students=StudentProfile.objects.all()
    return render(request,'accounts/student_list.html',{'students':students})

                  



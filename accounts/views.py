from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import StudentProfile
from django.shortcuts import redirect
from .forms import StudentProfileForm


@login_required

def student_list(request):
    students=StudentProfile.objects.all()
    return render(request,'accounts/student_list.html',{'students':students})


@login_required
def student_add(request):
    if not (request.user.is_admin or request.user.is_warden):
        return redirect('dashboard:home')
    if request.method=='POST':
        form=StudentProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:student_list')
    else:
        form=StudentProfileForm()
    return render(request,'accounts/student_form.html',{'form':form})




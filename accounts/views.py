from django.contrib.auth.decorators import login_required
from .models import StudentProfile,User
from django.shortcuts import redirect,render
from .forms import StudentProfileForm,StudentUserForm
from django.shortcuts import get_object_or_404



@login_required

def student_list(request):
    students=StudentProfile.objects.all()
    return render(request,'accounts/student_list.html',{'students':students})


@login_required
def student_add(request):
    if not (request.user.is_admin or request.user.is_warden):
        return redirect('dashboard:home')
    
    if request.method=='POST':
        user_form=StudentUserForm(request.POST)
        profile_form=StudentProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():

           new_user=user_form.save(commit=False)
           new_user.role=User.Role.STUDENT
           new_user.save()

           new_profile = profile_form.save(commit=False)
           new_profile.user = new_user
           new_profile.save()

           return redirect('accounts:student_list')
    else:
        user_form = StudentUserForm()
        profile_form = StudentProfileForm()

    return render(request, 'accounts/student_form.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })


@login_required

def student_edit(request,pk):
    if not(request.user.is_admin) and (request.user.is_warden):
        return redirect('dashboard:home')
    student=get_object_or_404(StudentProfile,pk=pk)

    if request.method=='POST':
        profile_form=StudentProfileForm(request.POST,instance=student)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('accounts:student_list')
    else:
        profile_form=StudentProfileForm(instance=student)
    return render(request,'accounts/student_edit.html',{
        'profile_form':profile_form,
        'student':student,

    })

    




        


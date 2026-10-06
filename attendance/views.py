from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Attendance
from .forms import AttendanceForm


@login_required
def attendance_list(request):

    if request.user.is_student:
        attendance = Attendance.objects.filter(
            student=request.user.student_profile
        ).order_by('-date')
    else:
        attendance = Attendance.objects.all().order_by('-date')

    return render(
        request,
        'attendance/attendance_list.html',
        {
            'attendance': attendance,
            'is_student': request.user.is_student,
        }
    )

@login_required
def my_attendance(request):
    if not request.user.is_student:
        return redirect('dashboard:home')

    attendance = Attendance.objects.filter(
        student=request.user.student_profile
    ).order_by('-date')

    return render(
        request,
        'attendance/my_attendance.html',
        {
            'attendance': attendance,
        }
    )


@login_required
def attendance_add(request):
    if not (request.user.is_admin or request.user.is_warden):
        return redirect('dashboard:home')

    if request.method == 'POST':
        form = AttendanceForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('attendance:attendance_list')

    else:
        form = AttendanceForm()

    return render(
        request,
        'attendance/attendance_form.html',
        {'form': form}
    )


@login_required
def attendance_edit(request, pk):
    if not (request.user.is_admin or request.user.is_warden):
        return redirect('dashboard:home')

    attendance = get_object_or_404(Attendance, pk=pk)

    if request.method == 'POST':
        form = AttendanceForm(
            request.POST,
            instance=attendance
        )

        if form.is_valid():
            form.save()
            return redirect('attendance:attendance_list')

    else:
        form = AttendanceForm(instance=attendance)

    return render(
        request,
        'attendance/attendance_form.html',
        {'form': form}
    )


@login_required
def attendance_delete(request, pk):
    if not (request.user.is_admin or request.user.is_warden):
        return redirect('dashboard:home')

    attendance = get_object_or_404(Attendance, pk=pk)

    if request.method == 'POST':
        attendance.delete()
        return redirect('attendance:attendance_list')

    return render(
        request,
        'attendance/attendance_confirm_delete.html',
        {'attendance': attendance}
    )
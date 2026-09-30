from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Complaint
from .forms import ComplaintForm, ComplaintStatusForm


@login_required
def complaint_list(request):
    if request.user.is_student:
        complaints = Complaint.objects.filter(student=request.user.student_profile)
    else:
        complaints = Complaint.objects.all()

    return render(
        request,
        'complaints/complaint_list.html',
        {'complaints': complaints}
    )


@login_required
def complaint_add(request):

    if request.method == 'POST':

        if request.user.is_student:
            # Student cannot choose another student
            form = ComplaintForm(request.POST)
            form.fields.pop('student', None)

            if form.is_valid():
                complaint = form.save(commit=False)
                complaint.student = request.user.student_profile
                complaint.save()

                return redirect('complaints:complaint_list')

        else:
            # Admin/Warden can select a student
            form = ComplaintForm(request.POST)

            if form.is_valid():
                form.save()

                return redirect('complaints:complaint_list')

    else:

        if request.user.is_student:
            form = ComplaintForm()
            form.fields.pop('student', None)

        else:
            form = ComplaintForm()

    return render(
        request,
        'complaints/complaint_form.html',
        {'form': form}
    )


@login_required
def complaint_edit(request, pk):

    if not (request.user.is_admin or request.user.is_warden):
        return redirect('dashboard:home')

    complaints = get_object_or_404(Complaint, pk=pk)

    if request.method == 'POST':
        form = ComplaintForm(request.POST, instance=complaints)

        if form.is_valid():
            form.save()
            return redirect('complaints:complaint_list')

    else:
        form = ComplaintForm(instance=complaints)

    return render(
        request,
        'complaints/complaint_form.html',
        {'form': form}
    )


@login_required
def complaint_delete(request, pk):

    if not (request.user.is_admin or request.user.is_warden):
        return redirect('dashboard:home')

    complaints = get_object_or_404(Complaint, pk=pk)

    if request.method == 'POST':
        complaints.delete()
        return redirect('complaints:complaint_list')

    return render(
        request,
        'complaints/complaint_confirm_delete.html',
        {'complaints': complaints}
    )


@login_required
def update_status(request, pk):

    if not (request.user.is_admin or request.user.is_warden):
        return redirect('dashboard:home')

    complaint = get_object_or_404(Complaint, pk=pk)

    if request.method == 'POST':
        form = ComplaintStatusForm(
            request.POST,
            instance=complaint
        )

        if form.is_valid():
            form.save()
            return redirect('complaints:complaint_list')

    else:
        form = ComplaintStatusForm(instance=complaint)

    return render(
        request,
        'complaints/update_status.html',
        {
            'form': form,
            'complaint': complaint
        }
    )



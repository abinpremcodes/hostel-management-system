from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Complaint
from .forms import ComplaintForm, ComplaintStatusForm


@login_required
def complaint_list(request):

    if request.user.is_student:
        complaints = Complaint.objects.filter(
            student=request.user.student_profile
        )
    else:
        complaints = Complaint.objects.all()

    return render(
        request,
        'complaints/complaint_list.html',
        {
            'complaints': complaints
        }
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

                messages.success(
                    request,
                    'Complaint submitted successfully!'
                )

                return redirect('complaints:complaint_list')

        else:

            # Admin/Warden can select a student
            form = ComplaintForm(request.POST)

            if form.is_valid():

                form.save()

                messages.success(
                    request,
                    'Complaint added successfully!'
                )

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
        {
            'form': form
        }
    )


@login_required
def complaint_edit(request, pk):

    complaint = get_object_or_404(
        Complaint,
        pk=pk
    )

    # Students can edit only their own complaints
    if request.user.is_student:

        if complaint.student != request.user.student_profile:
            return redirect('dashboard:home')

    # Only Admin/Warden or the complaint owner can edit
    elif not (request.user.is_admin or request.user.is_warden):

        return redirect('dashboard:home')

    if request.method == 'POST':

        form = ComplaintForm(
            request.POST,
            instance=complaint
        )

        # Students must not be able to change the student
        if request.user.is_student:
            form.fields.pop('student', None)

        if form.is_valid():

            updated_complaint = form.save(commit=False)

            # Always keep the original student for student edits
            if request.user.is_student:
                updated_complaint.student = request.user.student_profile

            updated_complaint.save()

            messages.success(
                request,
                'Complaint updated successfully!'
            )

            return redirect('complaints:complaint_list')

    else:

        form = ComplaintForm(
            instance=complaint
        )

        if request.user.is_student:
            form.fields.pop('student', None)

    return render(
        request,
        'complaints/complaint_form.html',
        {
            'form': form,
            'complaint': complaint
        }
    )


@login_required
def complaint_delete(request, pk):

    # Only Admin/Warden can delete complaints
    if not (request.user.is_admin or request.user.is_warden):
        return redirect('dashboard:home')

    complaint = get_object_or_404(
        Complaint,
        pk=pk
    )

    if request.method == 'POST':

        complaint.delete()

        messages.success(
            request,
            'Complaint deleted successfully!'
        )

        return redirect('complaints:complaint_list')

    return render(
        request,
        'complaints/complaint_confirm_delete.html',
        {
            'complaints': complaint
        }
    )


@login_required
def update_status(request, pk):

    # Only Admin/Warden can update complaint status
    if not (request.user.is_admin or request.user.is_warden):
        return redirect('dashboard:home')

    complaint = get_object_or_404(
        Complaint,
        pk=pk
    )

    if request.method == 'POST':

        form = ComplaintStatusForm(
            request.POST,
            instance=complaint
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Complaint status updated successfully!'
            )

            return redirect('complaints:complaint_list')

    else:

        form = ComplaintStatusForm(
            instance=complaint
        )

    return render(
        request,
        'complaints/update_status.html',
        {
            'form': form,
            'complaint': complaint
        }
    )



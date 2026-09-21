from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Complaint
from . forms import ComplaintForm,ComplaintStatusForm


@login_required
def complaint_list(request):
    complaints=Complaint.objects.all()
    return render(request,'complaints/complaint_list.html',{'complaints':complaints})


@login_required
def complaint_add(request):
    if not(request.user.is_admin or request.user.is_warden):
        return redirect('dashboard:home')


    if request.method=='POST':
        form=ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('complaints:complaint_list')

    else:
        form=ComplaintForm()
    return render(request,'complaints/complaint_form.html',{'form':form})


@login_required
def complaint_edit(request,pk):
    if not (request.user.is_admin or request.user.is_warden):
        return redirect('dashboard:home')

    complaints=get_object_or_404(Complaint,pk=pk)

    if request.method=='POST':
        form=ComplaintForm(request.POST,instance=complaints)
        if form.is_valid():
            form.save()
            return redirect('complaints:complaint_list')

    else:
        form=ComplaintForm(instance=complaints)
    return render(request,'complaints/complaint_form.html',{'form':form})

@login_required
def complaint_delete(request,pk):
    if not(request.user.is_admin or request.user.is_warden):
        return redirect('dashboard:home')

    complaints=get_object_or_404(Complaint,pk=pk)

    if request.method=='POST':
        complaints.delete()
        return redirect('complaints:complaint_list')
    return render(request,'complaints/complaint_confirm_delete.html',{'complaints':complaints})


@login_required
def update_status(request, pk):
    if not (request.user.is_admin or request.user.is_warden):
        return redirect('dashboard:home')

    complaint = get_object_or_404(Complaint, pk=pk)

    if request.method == 'POST':
        form = ComplaintStatusForm(request.POST, instance=complaint)
        if form.is_valid():
            form.save()
            return redirect('complaints:complaint_list')
    else:
        form = ComplaintStatusForm(instance=complaint)

    return render(request, 'complaints/update_status.html', {'form': form, 'complaint': complaint})


    

        





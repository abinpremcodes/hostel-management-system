from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Allocation
from .forms import AllocationForm,TransferForm
from django.shortcuts import get_object_or_404
from django.utils import timezone
from hostel.models import Bed


@login_required
def allocation_list(request):
    allocations=Allocation.objects.all()
    return render (request,'allocations/allocation_list.html',{'allocations':allocations})


@login_required
def allocation_add(request):
    if not(request.user.is_admin or request.user.is_warden):
        return redirect('dashboard:home')

    if request.method=='POST':
        form=AllocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allocations:allocation_list')
    else:
        form=AllocationForm()
    return render(request,'allocations/allocation_form.html',{'form':form})



@login_required
def allocation_vacate(request,pk):
    if not (request.user.is_admin or request.user.is_warden):
        return redirect('dashboard:home')

    allocation=get_object_or_404(Allocation,pk=pk)

    if request.method=='POST':
        allocation.status=Allocation.Status.VACATED
        allocation.vacated_date=timezone.now().date()
        allocation.save()

        allocation.bed.status=Bed.Status.AVAILABLE
        allocation.bed.save()

        return redirect('allocations:allocation_list')
    return render(request,'allocations/allocation_confirm_vacate.html',{'allocation':allocation})


@login_required
def allocation_transfer(request,pk):
    if not (request.user.is_admin or request.user.is_warden):
        return redirect('dashboard:home')

    allocation=get_object_or_404(Allocation,pk=pk)

    if request.method=='POST':
        form=TransferForm(request.POST)
        if form.is_valid():
            new_bed = form.cleaned_data['new_bed']


            allocation.status=Allocation.Status.VACATED
            allocation.vacated_date=timezone.now().date()
            allocation.save()

            allocation.bed.status=Bed.Status.AVAILABLE
            allocation.save()


            Allocation.objects.create(student=allocation.student, bed=new_bed)

            new_bed.status = Bed.Status.OCCUPIED
            new_bed.save()

            return redirect('allocations:allocation_list')
    else:
        form=TransferForm()
    return render(request,'allocations/allocation_transfer.html',{'form':form,'allocation':allocation})







    


from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Allocation
from .forms import AllocationForm

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

    


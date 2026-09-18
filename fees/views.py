from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Fee
from .forms import FeeForm


@login_required
def fee_list(request):
    fees=Fee.objects.all()
    return render(request,'fees/fee_list.html',{'fees':fees})

@login_required
def fee_add(request):
    if not(request.user.is_admin or request.user.is_warden):
        return redirect('dashboard:home')

    if request.method=='POST':
        form=FeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fees:fee_list')
    else:
        form=FeeForm()
    return render(request,'fees/fee_form.html',{'form':form})



@login_required
def fee_edit(request,pk):
    if not(request.user.is_admin or request.user.is_warden):
        return redirect('dashboard:home')

    fees=get_object_or_404(Fee,pk=pk)

    if request.method=='POST':
        form=FeeForm(request.POST,instance=fees)
        if form.is_valid():
            form.save()
            return redirect('fees:fee_list')
    else:
        form=FeeForm(instance=fees)
    return render(request,'fees/fee_form.html',{'form':form})


@login_required
def fee_delete(request,pk):
    if not(request.user.is_admin or request.user.is_warden):
        return redirect('dashboard:home')

    fees=get_object_or_404(Fee,pk=pk)

    if request.method=='POST':
        fees.delete()
        return redirect('fees:fee_list')

    return render(request,'fees/fee_confirm_delete.html',{'fees':fees})







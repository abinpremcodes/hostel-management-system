from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from .models import Building,Floor
from .forms import BuildingForm,FloorForm

@login_required
def building_list(request):
    buildings=Building.objects.all()
    return render(request,'hostel/building_list.html',{'buildings':buildings})


@login_required
def building_add(request):
    if not (request.user.is_admin or request.user.is_warden):
        return redirect('dashboard:home')

    if request.method=='POST':
        form=BuildingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hostel:building_list')
    else:
        form=BuildingForm()
    return render(request,'hostel/building_form.html',{'form':form})


@login_required
def building_edit(request,pk):
    if not(request.user.is_admin or request.user.is_warden):
        return redirect('dashboard:home')

    building=get_object_or_404(Building,pk=pk)

    if request.method=='POST':
        form=BuildingForm(request.POST,instance=building)
        if form.is_valid():
            form.save()
            return redirect('hostel:building_list')
    else:
        form=BuildingForm(instance=building)
    return render(request,'hostel/building_form.html',{'form':form})


@login_required
def building_delete(request,pk):
    if not(request.user.is_admin or request.user.is_warden):
        return redirect ('dashboard:home')

    building=get_object_or_404(Building,pk=pk)

    if request.method=='POST':
        building.delete()
        return redirect('hostel:building_list')

    return render(request,'hostel/building_confirm_delete.html',{'building':building})






@login_required
def floor_list(request):
    floors=Floor.objects.all()
    return render(request,'hostel/floor_list.html',{'floors':floors})


@login_required
def floor_add(request):
    if not(request.user.is_admin or request.user.is_warden):
        return redirect('dashboard:home')

    if request.method=='POST':
        form=FloorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hostel:floor_list')
    else:
        form=FloorForm()
    return render(request,'hostel/floor_form.html',{'form':form})

@login_required
def floor_edit(request,pk):
    if not(request.user.is_admin or request.user.is_warden):
        return redirect('dashboard:home')
    floor=get_object_or_404(Floor,pk=pk)

    if request.method=='POST':
        form=FloorForm(request.POST,instance=floor)
        if form.is_valid():
            form.save()
            return redirect('hostel:floor_list')
    else:
        form=FloorForm(instance=floor)
    return render(request,'hostel/floor_form.html',{'form':form})

@login_required
def floor_delete(request,pk):
    if not(request.user.is_admin or request.user.is_warden):
        return redirect('dashboard:home')

    floor=get_object_or_404(Floor,pk=pk)

    if request.method=='POST':
        floor.delete()
        return redirect('hostel:floor_list')
    return render(request,'hostel/floor_confirm_delete.html',{'floor':floor})

    











        






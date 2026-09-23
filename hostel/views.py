from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from .models import Building,Floor,Room,Bed
from .forms import BuildingForm,FloorForm,RoomForm,BedForm
from django.http import JsonResponse


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





@login_required
def room_list(request):
    rooms=Room.objects.all()
    return render(request,'hostel/room_list.html',{'rooms':rooms})


@login_required
def room_add(request):
    if not(request.user.is_admin or request.user.is_warden):
        return redirect('dashboard:home')

    if request.method=='POST':
        form=RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hostel:room_list')
    else:
        form=RoomForm()
    return render(request,'hostel/room_form.html',{'form':form})


@login_required
def room_edit(request,pk):
    if not(request.user.is_admin or request.user.is_warden):
        return redirect('dashboard:home')

    room=get_object_or_404(Room,pk=pk)

    if request.method=='POST':
        form=RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('hostel:room_list')
    else:
        form=RoomForm(instance=room)
    return render(request,'hostel/room_form.html',{'form':form})


@login_required
def room_delete(request,pk):
    if not(request.user.is_admin or request.user.is_warden):
        return redirect('dashboard:home')

    room=get_object_or_404(Room,pk=pk)

    if request.method=='POST':
        room.delete()
        return redirect('hostel:room_list')
    return render(request,'hostel/room_confirm_delete.html',{'room':room})




@login_required
def bed_list(request):
    beds=Bed.objects.all()
    return render(request,'hostel/bed_list.html',{'beds':beds})


@login_required
def bed_add(request):
    if not(request.user.is_admin or request.user.is_warden):
        return redirect('dashboard:home')

    if request.method=='POST':
        form=BedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hostel:bed_list')
    else:
        form=BedForm()
    return render(request,'hostel/bed_form.html',{'form':form})


@login_required
def bed_edit(request,pk):
    if not(request.user.is_admin or request.user.is_warden):
        return redirect('dashboard:home')

    bed=get_object_or_404(Bed,pk=pk)

    if request.method=='POST':
        form=BedForm(request.POST,instance=bed)
        if form.is_valid():
            form.save()
            return redirect('hostel:bed_list')
    else:
        form=BedForm(instance=bed)
    return render(request,'hostel/bed_form.html',{'form':form})


@login_required
def  bed_delete(request,pk):
    if not(request.user.is_admin or request.user.is_warden):
        return redirect('dashboard:home')

    bed=get_object_or_404(Bed,pk=pk)

    if request.method=='POST':
        bed.delete()
        return redirect('hostel:bed_list')
    return render(request,'hostel/bed_confirm_delete.html',{'bed':bed})


@login_required
def api_rooms_by_building(request, building_id):
    rooms = Room.objects.filter(floor__building_id=building_id)
    data = [{'id': r.id, 'label': f"{r.room_number} ({r.floor})"} for r in rooms]
    return JsonResponse({'rooms': data})


@login_required
def api_beds_by_room(request, room_id):
    beds = Bed.objects.filter(room_id=room_id, status=Bed.Status.AVAILABLE)
    data = [{'id': b.id, 'label': f"Bed {b.bed_number}"} for b in beds]
    return JsonResponse({'beds': data})



@login_required
def api_buildings(request):
    buildings = Building.objects.all()
    data = [{'id': b.id, 'label': b.name} for b in buildings]
    return JsonResponse({'buildings': data})


    














        






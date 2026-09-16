from django import forms
from .models import Building,Floor,Room,Bed

class BuildingForm(forms.ModelForm):
    class Meta:
        model=Building
        fields=['name','address']


class FloorForm(forms.ModelForm):
    class Meta:
        model=Floor
        fields=['building','floor_number']


class RoomForm(forms.ModelForm):
    class Meta:
        model=Room
        fields=['floor','room_number','room_type','capacity','status']


class BedForm(forms.ModelForm):
    class Meta:
        model=Bed
        fields=['room', 'bed_number', 'status']









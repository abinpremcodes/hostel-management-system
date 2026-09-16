from django import forms
from .models import Building,Floor

class BuildingForm(forms.ModelForm):
    class Meta:
        model=Building
        fields=['name','address']


class FloorForm(forms.ModelForm):
    class Meta:
        model=Floor
        fields=['building','floor_number']

        



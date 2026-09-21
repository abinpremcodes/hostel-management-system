from django import forms
from .models import Complaint


class ComplaintForm(forms.ModelForm):
    class Meta:
        model=Complaint
        fields=['student','category','priority','title','description']


class ComplaintStatusForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['status', 'assigned_to']


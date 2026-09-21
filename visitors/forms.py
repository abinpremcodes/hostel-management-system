from django import forms
from .models import Visitor



class VisitorForm(forms.ModelForm):
    class Meta:
        model=Visitor
        fields=['student', 'visitor_name', 'phone', 'purpose']

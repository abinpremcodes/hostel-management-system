from django import forms
from .models import Fee

class FeeForm(forms.ModelForm):
    class Meta:
        model=Fee
        fields=['student','fee_type','amount','due_date']

        
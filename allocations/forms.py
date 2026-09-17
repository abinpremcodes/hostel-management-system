from django import forms
from .models import Allocation
from hostel.models import Bed


class AllocationForm(forms.ModelForm):
    class Meta:
        model = Allocation
        fields = ['student', 'bed']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bed'].queryset = Bed.objects.filter(status=Bed.Status.AVAILABLE)
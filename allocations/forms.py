from django import forms
from .models import Allocation
from hostel.models import Bed


class AllocationForm(forms.ModelForm):
    class Meta:
        model = Allocation
        fields = ['student', 'bed']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['bed'].queryset = Bed.objects.filter(
            status=Bed.Status.AVAILABLE
        )


class TransferForm(forms.Form):
    new_bed = forms.ModelChoiceField(
        queryset=Bed.objects.none(),
        label='New Bed'
    )

    def __init__(self, *args, **kwargs):
        allocation = kwargs.pop('allocation', None)
        super().__init__(*args, **kwargs)

        beds = Bed.objects.filter(
            status=Bed.Status.AVAILABLE
        )

        if allocation:
            # Exclude all beds from the student's current room
            beds = beds.exclude(
                room=allocation.bed.room
            )

        self.fields['new_bed'].queryset = beds
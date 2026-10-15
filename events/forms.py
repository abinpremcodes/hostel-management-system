from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            "title",
            "description",
            "venue",
            "date",
            "time",
        ]
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter event title",
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "Enter event description",
            }),
            "venue": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter event venue",
            }),
            "date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date",
            }),
            "time": forms.TimeInput(attrs={
                "class": "form-control",
                "type": "time",
            }),
        }
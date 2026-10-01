from django import forms
from .models import Visitor


class VisitorForm(forms.ModelForm):

    class Meta:
        model = Visitor
        fields = [
            'student',
            'visitor_name',
            'relation',
            'phone',
            'purpose'
        ]

        labels = {
            'student': 'Student',
            'visitor_name': 'Visitor Name',
            'relation': 'Relation',
            'phone': 'Phone',
            'purpose': 'Purpose',
        }

        widgets = {
            'student': forms.Select(attrs={
                'class': 'form-select'
            }),

            'visitor_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter visitor name'
            }),

            'relation': forms.Select(attrs={
                'class': 'form-select'
            }),

            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number',
                'inputmode': 'numeric',
                'maxlength': '10'
            }),

            'purpose': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Example: Meet student'
            }),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '').strip()

        if not phone.isdigit():
            raise forms.ValidationError(
                'Phone number must contain numbers only.'
            )

        if len(phone) != 10:
            raise forms.ValidationError(
                'Phone number must contain exactly 10 digits.'
            )

        return phone
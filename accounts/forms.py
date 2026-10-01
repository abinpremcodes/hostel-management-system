from django import forms
from .models import StudentProfile, User
from django.contrib.auth.forms import UserCreationForm


class StudentUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'phone',
            'password1',
            'password2'
        ]

        widgets = {
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number',
                'inputmode': 'numeric',
                'maxlength': '10'
            }),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '').strip()

        if phone and not phone.isdigit():
            raise forms.ValidationError(
                'Phone number must contain numbers only.'
            )

        if phone and len(phone) != 10:
            raise forms.ValidationError(
                'Phone number must contain exactly 10 digits.'
            )

        return phone


class StudentProfileForm(forms.ModelForm):

    class Meta:
        model = StudentProfile
        fields = [
            'student_id',
            'course',
            'year',
            'guardian_name',
            'guardian_phone',
            'address'
        ]

        widgets = {
            'guardian_phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter guardian phone number',
                'inputmode': 'numeric',
                'maxlength': '10'
            }),
        }

    def clean_guardian_name(self):
        name = self.cleaned_data.get('guardian_name', '').strip()

        if not name:
            raise forms.ValidationError(
                'Guardian name is required.'
            )

        allowed_characters = set(
            "abcdefghijklmnopqrstuvwxyz"
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            " .'-"
        )

        if any(character not in allowed_characters for character in name):
            raise forms.ValidationError(
                'Guardian name can contain letters, spaces, periods, hyphens, and apostrophes only.'
            )

        return name

    def clean_guardian_phone(self):
        phone = self.cleaned_data.get('guardian_phone', '').strip()

        if not phone.isdigit():
            raise forms.ValidationError(
                'Guardian phone number must contain numbers only.'
            )

        if len(phone) != 10:
            raise forms.ValidationError(
                'Guardian phone number must contain exactly 10 digits.'
            )

        return phone
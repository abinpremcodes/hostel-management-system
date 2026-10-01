# from django import forms
# from .models import Complaint


# class ComplaintForm(forms.ModelForm):
#     class Meta:
#         model=Complaint
#         fields=['student','category','priority','title','description']


# class ComplaintStatusForm(forms.ModelForm):
#     class Meta:
#         model = Complaint
#         fields = ['status', 'assigned_to']


from django import forms

from .models import Complaint


class ComplaintForm(forms.ModelForm):

    class Meta:
        model = Complaint
        fields = ['student', 'category', 'priority', 'title', 'description']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter complaint title',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe your complaint',
                'rows': 5,
            }),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title', '').strip()

        if not title:
            raise forms.ValidationError('Complaint title is required.')

        return title

    def clean_description(self):
        description = self.cleaned_data.get('description', '').strip()

        if not description:
            raise forms.ValidationError('Complaint description is required.')

        return description


class ComplaintStatusForm(forms.ModelForm):

    class Meta:
        model = Complaint
        fields = ['status', 'assigned_to']

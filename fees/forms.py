from django import forms
from .models import Fee,Payment

class FeeForm(forms.ModelForm):
    class Meta:
        model=Fee
        fields=['student','fee_type','amount','due_date']


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'payment_method', 'transaction_ref']




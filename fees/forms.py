
from django import forms
from .models import Fee, Payment


class FeeForm(forms.ModelForm):

    class Meta:
        model = Fee
        fields = ['student', 'fee_type', 'amount', 'due_date']

        widgets = {
            'amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter fee amount',
                'min': '0.01',
                'step': '0.01'
            }),
            'due_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')

        if amount is None or amount <= 0:
            raise forms.ValidationError(
                'Fee amount must be greater than 0.'
            )

        return amount


class PaymentForm(forms.ModelForm):

    class Meta:
        model = Payment
        fields = ['amount', 'payment_method', 'transaction_ref']

        widgets = {
            'amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter payment amount',
                'min': '0.01',
                'step': '0.01'
            }),
        }

    def __init__(self, *args, **kwargs):
        self.fee = kwargs.pop('fee', None)
        super().__init__(*args, **kwargs)

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')

        if amount is None or amount <= 0:
            raise forms.ValidationError(
                'Payment amount must be greater than 0.'
            )

        if self.fee:
            remaining_balance = self.fee.balance

            if amount > remaining_balance:
                raise forms.ValidationError(
                    f'Payment cannot exceed the remaining balance of ₹{remaining_balance}.'
                )

        return amount


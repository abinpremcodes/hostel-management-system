from django.db import models
from django.utils import timezone
from accounts.models import StudentProfile


class Fee (models.Model):
    class FeeType(models.TextChoices):
        HOSTEL='HOSTEL','Hostel fee'
        MESS='MESS','Mess fee'
        MAINTENANCE='MAINTENANCE','Maintenance fee'
        OTHER='OTHER','other'


    class Status(models.TextChoices):
        PAID='PAID','paid'
        PENDING='PENDING','pending'
        OVERDUE='OVERDUE','overdue'

    student=models.ForeignKey(StudentProfile,on_delete=models.CASCADE,related_name='fees')
    fee_type=models.CharField(max_length=15,choices=FeeType.choices,default=FeeType.HOSTEL)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    due_date=models.DateField()
    status=models.CharField(max_length=10,choices=Status.choices,default=Status.PENDING)

    def __str__(self):
        return f"{self.student} - {self.get_fee_type_display()} - {self.status}"

    def refresh_status(self):
        total_paid = sum(p.amount for p in self.payments.all())
        if total_paid >= self.amount:
            self.status = self.Status.PAID
        elif self.due_date < timezone.now().date():
            self.status = self.Status.OVERDUE
        else:
            self.status = self.Status.PENDING
        self.save()


class Payment(models.Model):
    class Method(models.TextChoices):
        CASH='CASH','Cash'
        CARD='CARD','Card'
        UPI='UPI','UPI'
        BANK_TRANSFER='BANK_TRANSFER','Bank transfer'

    fee=models.ForeignKey(Fee,on_delete=models.CASCADE,related_name='payments')
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    payment_method=models.CharField(max_length=15,choices=Method.choices,default=Method.CASH)
    transaction_ref=models.CharField(max_length=16,blank=True)
    paid_at=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"payment {self.amount} for {self.fee}"


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.fee.refresh_status()
    


    



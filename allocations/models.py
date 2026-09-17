from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from accounts.models import StudentProfile
from hostel.models import Bed


class Allocation(models.Model):
    class Status (models.TextChoices):
        ACTIVE='ACTIVE', 'Active'
        VACATED='VACATED','Vacated'

    student=models.ForeignKey(StudentProfile,on_delete=models.CASCADE,related_name='allocations')
    bed=models.ForeignKey(Bed,on_delete=models.CASCADE,related_name='allocations')
    allocated_date=models.DateField(default=timezone.now)
    vacated_date=models.DateField(null=True,blank=True)
    status=models.CharField(max_length=10,choices=Status.choices,default=Status.ACTIVE)


    def __str__(self):
        return f"{self.student} -> {self.bed} ({self.status})"


    def clean(self):
        if self.status == self.Status.ACTIVE:
            # Rule: a student cannot have multiple active allocations
            student_clash = Allocation.objects.filter(
                student=self.student, status=self.Status.ACTIVE
            ).exclude(pk=self.pk)
            if student_clash.exists():
                raise ValidationError("This student already has an active room allocation.")

            # Rule: a bed cannot be allocated to more than one active student
            bed_clash = Allocation.objects.filter(
                bed=self.bed, status=self.Status.ACTIVE
            ).exclude(pk=self.pk)
            if bed_clash.exists():
                raise ValidationError("This bed is already occupied by another active student.")

    

    

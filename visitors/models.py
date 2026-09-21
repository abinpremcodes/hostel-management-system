from django.db import models
from django.utils import timezone
from accounts .models import StudentProfile

class Visitor(models.Model):
    student=models.ForeignKey(StudentProfile,on_delete=models.CASCADE,related_name='visitors')
    visitor_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    purpose=models.CharField(max_length=200,blank=True)
    check_in=models.DateTimeField(default=timezone.now)
    check_out=models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return f" {self.visitor_name} visiting {self.student}"

    @property
    def is_checked_in(self):
        return self.check_out is None




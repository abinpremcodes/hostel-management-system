from django.db import models
from accounts.models import StudentProfile

class Attendance(models.Model):
    class Status(models.TextChoices):
        PRESENT='PRESENT','Present'
        ABSENT='ABSENT','Absent'


    student=models.ForeignKey(StudentProfile,on_delete=models.CASCADE,related_name='attendance_records')
    date=models.DateField()
    status=models.CharField(max_length=15,choices=Status.choices,default=Status.PRESENT)


    class Meta:
        unique_together=('student','date')

    def __str__(self):
        return f"Attendance {self.student} - {self.date} - {self.get_status_display()}"
    


    
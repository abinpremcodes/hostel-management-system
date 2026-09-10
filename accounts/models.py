from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN='ADMIN','admin',
        WARDEN='WARDEN','warden',
        STUDENT='STUDENT','student',

    role=models.CharField(max_length=10,choices=Role.choices,default=Role.STUDENT)
    phone=models.CharField(max_length=15,blank=True)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"


class StudentProfile(models.Model):
    class YearChoice(models.IntegerChoices):
        FIRST=1,'1st Year',
        SECOND=2,'2nd Year',
        THIRD=3,'3rd Year',
        FOUR=4,'4th Year',


    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='student_profile')
    student_id=models.CharField(max_length=20,unique=True)
    course=models.CharField(max_length=100)
    year=models.IntegerField(choices=YearChoice.choices,default=YearChoice.FIRST)
    guardian_name=models.CharField(max_length=20)
    guardian_phone=models.CharField(max_length=15)
    address=models.TextField(blank=True)
    date_joined_hostel=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_id} - {self.user.username}"




    




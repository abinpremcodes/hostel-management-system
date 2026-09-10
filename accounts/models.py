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

    




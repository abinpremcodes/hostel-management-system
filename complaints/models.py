from django.db import models
from django.utils import timezone
from accounts .models import StudentProfile,User

class Complaint(models.Model):
    class Category(models.TextChoices):
        ELECTRICAL='ELECTRICAL','Electrical'
        PLUMBING='PLUMBING','Plumbing'
        CLEANLINESS='CLEANLINESS','Cleanliness'
        FOOD='FOOD','Food/Mess'
        SECURITY='SECURITY','Security'
        OTHER='OTHER','Other'

    class Priority(models.TextChoices):
        LOW='LOW','Low'
        MEDIUM='MEDIUM','Medium'
        HIGH='HIGH','High'

    class Status(models.TextChoices):
        PENDING='PENDING','Pending'
        IN_PROGRESS='IN_PROGRESS','In_progress'
        RESOLVED='RESOLVED','Resolved'

    student=models.ForeignKey(StudentProfile,on_delete=models.CASCADE,related_name='complaints')
    category=models.CharField(max_length=15, choices=Category.choices,default=Category.OTHER)
    priority=models.CharField(max_length=20,choices=Priority.choices,default=Priority.MEDIUM)
    title=models.CharField(max_length=150)
    description=models.TextField()
    status=models.CharField(max_length=15,choices=Status.choices,default=Status.PENDING)
    assigned_to=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name='assigned_complaints')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.title} ({self.status})"



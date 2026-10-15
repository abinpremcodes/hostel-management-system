from django.db import models

class Event(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    venue=models.CharField(max_length=200)
    date=models.DateField()
    time=models.TimeField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=["date","time"]

    def __str__(self):
        return self.title


from django.db import models
from django.core.exceptions import ValidationError


class Building(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Floor(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='floors')
    floor_number = models.IntegerField()

    class Meta:
        unique_together = ('building', 'floor_number')

    def __str__(self):
        return f"{self.building.name} - Floor {self.floor_number}"


class Room(models.Model):
    class RoomType(models.TextChoices):
        SINGLE = 'SINGLE', 'Single'
        DOUBLE = 'DOUBLE', 'Double'
        DORM = 'DORM', 'Dormitory'

    class Status(models.TextChoices):
        AVAILABLE = 'AVAILABLE', 'Available'
        FULL = 'FULL', 'Full'
        MAINTENANCE = 'MAINTENANCE', 'Under Maintenance'

    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, related_name='rooms')
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=10, choices=RoomType.choices, default=RoomType.DOUBLE)
    capacity = models.PositiveIntegerField()
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.AVAILABLE)

    class Meta:
        unique_together = ('floor', 'room_number')

    def __str__(self):
        return f"Room {self.room_number} ({self.floor})"


class Bed(models.Model):
    class Status(models.TextChoices):
        AVAILABLE = 'AVAILABLE', 'Available'
        OCCUPIED = 'OCCUPIED', 'Occupied'
        MAINTENANCE = 'MAINTENANCE', 'Under Maintenance'

    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='beds')
    bed_number = models.CharField(max_length=10)
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.AVAILABLE)

    class Meta:
        unique_together = ('room', 'bed_number')

    def __str__(self):
        return f"Bed {self.bed_number} - {self.room}" 

    def clean(self):
        if self.room_id:
            existing_beds = Bed.objects.filter(room=self.room).exclude(pk=self.pk).count()
            if existing_beds + 1 > self.room.capacity:
                raise ValidationError(
                    f"Room {self.room.room_number} already has the maximum "
                    f"{self.room.capacity} bed(s)."
                )
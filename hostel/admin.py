from django.contrib import admin
from .models import Building,Floor,Room,Bed

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display=('name','address')

@admin.register(Floor)
class FloorAdmin(admin.ModelAdmin):
    list_display=('building','floor_number')

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display=('room_number','floor','room_type','capacity','status')

@admin.register(Bed)
class BedAdmin(admin.ModelAdmin):
    list_display=('bed_number','room','status')
    



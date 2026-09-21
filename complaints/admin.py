from django.contrib import admin
from.models import Complaint



@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display='title','student','category','priority','status','assigned_to','created_at'

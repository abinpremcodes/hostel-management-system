from django.contrib import admin
from .models import Visitor

@admin.register
class VisitorAdmin(admin.ModelAdmin):
    class Meta:
        model=Visitor
        fields='student','visitor_name','phone','check_in','check_out'
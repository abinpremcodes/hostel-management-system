from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,StudentProfile


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display=('username','email','role','is_staff')
    fieldsets=UserAdmin.fieldsets + (
    ('Role Info',{'fields': ('role', 'phone')}),
    )

@admin.register(StudentProfile)

class StudentProfileAdmin(admin.ModelAdmin):
    list_display=('student_id','user','course','year')



    
    


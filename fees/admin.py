from django.contrib import admin
from .models import Fee ,Payment

class PaymentINline(admin.TabularInline):
    model=Payment
    extra=0

@admin.register(Fee)
class AdminFee(admin.ModelAdmin):
    list_display=('student','fee_type','amount','due_date','status')
    inlines=[PaymentINline]

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display=('fee','amount','payment_method','paid_at')



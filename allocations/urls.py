from django.urls import path
from . import views


app_name='allocations'

urlpatterns=[
    path('',views.allocation_list,name='allocation_list'),
    path('add/',views.allocation_add,name='allocation_add'),


]
from django.urls import path
from . import views


app_name='allocations'

urlpatterns=[
    path('',views.allocation_list,name='allocation_list'),
    path('add/',views.allocation_add,name='allocation_add'),
    path('<int:pk>/vacate/', views.allocation_vacate, name='allocation_vacate'),
    path('<int:pk>/transfer/', views.allocation_transfer, name='allocation_transfer'),



]
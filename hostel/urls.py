from django.urls import path
from . import views

app_name='hostel'

urlpatterns=[
    path('buildings/',views.building_list,name='building_list'),
    path('buildings/add/',views.building_add,name='building_add'),
    path('buildings/<int:pk>/edit/',views.building_edit,name='building_edit'),
    path('buildings/<int:pk>/delete/',views.building_delete,name='building_delete'),

    
]
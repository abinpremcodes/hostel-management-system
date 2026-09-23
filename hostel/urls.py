from django.urls import path
from . import views

app_name='hostel'

urlpatterns=[
    path('buildings/',views.building_list,name='building_list'),
    path('buildings/add/',views.building_add,name='building_add'),
    path('buildings/<int:pk>/edit/',views.building_edit,name='building_edit'),
    path('buildings/<int:pk>/delete/',views.building_delete,name='building_delete'),


    path('floors/',views.floor_list,name='floor_list'),
    path('floors/add/',views.floor_add,name='floor_add'),
    path('floors/<int:pk>/edit/',views.floor_edit,name='floor_edit'),
    path('floors/<int:pk>/delete/',views.floor_delete,name='floor_delete'),



    path('rooms/',views.room_list,name='room_list'),
    path('rooms/add/',views.room_add,name='room_add'),
    path('rooms/<int:pk>/edit/',views.room_edit,name='room_edit'),
    path('rooms/<int:pk>/delete/',views.room_delete,name='room_delete'),



    path('beds/',views.bed_list,name='bed_list'),
    path('beds/add/',views.bed_add,name='bed_add'),
    path('beds/<int:pk>/edit/',views.bed_edit,name='bed_edit'),
    path('beds/<int:pk>/delete/',views.bed_delete,name='bed_delete'),
    path('api/rooms-by-building/<int:building_id>/', views.api_rooms_by_building, name='api_rooms_by_building'),
    path('api/beds-by-room/<int:room_id>/', views.api_beds_by_room, name='api_beds_by_room'),
    path('api/buildings/', views.api_buildings, name='api_buildings'),




    
]
from django.urls import path
from . import views

app_name='visitors'



urlpatterns=[
    path('',views.visitor_list,name='visitor_list'),
    path('add/',views.visitor_add,name='visitor_add'),
    path('<int:pk>/edit/',views.visitor_edit,name='visitor_edit'),
    path('<int:pk>/delete/',views.visitor_delete,name='visitor_delete'),
    path('<int:pk>/checkout/', views.visitor_checkout, name='visitor_checkout'),

         
]

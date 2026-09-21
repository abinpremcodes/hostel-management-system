from django.urls import path
from . import views


app_name='complaints'


urlpatterns=[
    path('',views.complaint_list,name='complaint_list'),
    path('add/',views.complaint_add,name='complaint_add'),
    path('<int:pk>/edit/',views.complaint_edit,name='complaint_edit'),
    path('<int:pk>/delete/',views.complaint_delete,name='complaint_delete'),
    path('<int:pk>/status/',views.update_status,name='update_status'),
    
]
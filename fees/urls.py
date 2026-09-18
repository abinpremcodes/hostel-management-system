from django.urls import path
from . import views

app_name='fees'


urlpatterns=[
    path('',views.fee_list,name='fee_list'),
    path('add/',views.fee_add,name='fee_add'),
    path('<int:pk>/edit/',views.fee_edit,name='fee_edit'),
    path('<int:pk>/delete/',views.fee_delete,name='fee_delete'),
    
]
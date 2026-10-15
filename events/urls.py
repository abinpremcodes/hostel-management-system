from django.urls import path
from . import views

app_name = "events"

urlpatterns = [
    # Student event viewing
    path("", views.event_list, name="my_events"),
    path("<int:pk>/", views.event_detail, name="event_detail"),

    # Admin/Warden event management
    path("manage/", views.manage_events, name="manage_events"),
    path("create/", views.create_event, name="create_event"),
    path("<int:pk>/edit/", views.edit_event, name="edit_event"),
    path("<int:pk>/delete/", views.delete_event, name="delete_event"),
]
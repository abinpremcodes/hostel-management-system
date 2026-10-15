
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('dashboard.urls')),
    path('hostel/', include('hostel.urls')),
    path('allocations/', include('allocations.urls')),
    path('fees/', include('fees.urls')),
    path('complaints/', include('complaints.urls')),
    path('visitors/', include('visitors.urls')),
    path('attendance/', include('attendance.urls')),
    path('events/', include('events.urls')),
]

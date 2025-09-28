from django.contrib import admin
from django.urls import path, include   # 👈 include added here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('appointments/', include('appointments.urls')),  # 👈 this links to your app
]

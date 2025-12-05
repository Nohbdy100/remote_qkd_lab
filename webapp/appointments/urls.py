from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.welcome, name='welcome'),  # root page
    path('appointment_scheduler/', views.appointment_scheduler, name='appointment_scheduler'),
    path('appointments/', views.appointments, name='appointments'),  # optional test view
]

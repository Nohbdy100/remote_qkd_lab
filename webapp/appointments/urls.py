from django.urls import path
from . import views

app_name = "appointments"

urlpatterns = [
    # Show all appointments
    path("", views.appointments, name="appointments"),

    # Schedule form
    path("appointment_scheduler/", views.appointment_scheduler, name="appointment_scheduler"),

    # Action buttons
    path("<int:pk>/cancel/", views.cancel_appointment, name="cancel"),
    path("<int:pk>/complete/", views.complete_appointment, name="complete"),
]

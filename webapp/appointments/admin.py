from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Appointment
from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("student", "faculty", "date", "time", "status")
    list_filter = ("status", "date", "faculty")
    search_fields = ("student__username", "faculty__username", "notes")

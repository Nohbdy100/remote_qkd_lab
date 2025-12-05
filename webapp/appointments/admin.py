from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Appointment
from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "date", "time")
    list_filter = ("student_id", "date", "notes")
    search_fields = ("student__username", "faculty__username", "notes")

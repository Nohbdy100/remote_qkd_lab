from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "date", "time")        # removed "status"
    list_filter = ("student_id", "date")                 # removed "status"
    search_fields = ("student_id", "notes")

from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student_appointments")
    faculty = models.ForeignKey(User, on_delete=models.CASCADE, related_name="faculty_appointments")
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student.username} with {self.faculty.username} on {self.date} at {self.time}"

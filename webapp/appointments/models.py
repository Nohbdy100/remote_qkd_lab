from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField(blank=True)
    student_id = models.TextField(max_length=6)

    def __str__(self):
        return f"{self.student.username} with {self.faculty.username} on {self.date} at {self.time}"

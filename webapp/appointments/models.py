from django.db import models

class Appointment(models.Model):
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField(blank=True)
    student_id = models.CharField(max_length=20)

    STATUS_CHOICES = [
        ('reserved', 'Reserved'),
        ('incomplete', 'Incomplete'),
        ('complete', 'Complete'),
        ('canceled', 'Canceled'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='reserved'
    )

    def __str__(self):
        return f"{self.student_id} – {self.date} {self.time}"

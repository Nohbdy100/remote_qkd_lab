from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Appointment
from .forms import AppointmentForm


def appointments(request):
    appts = Appointment.objects.all()
    return render(request, "appointments/my_appointments.html", {
        "appointments": appts,
    })


def appointment_scheduler(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Appointment successfully scheduled!")
            return redirect("appointments:appointments")
    else:
        form = AppointmentForm()

    return render(request, "appointments/reserve_slot.html", {
        "form": form,
    })


def cancel_appointment(request, pk):
    appt = get_object_or_404(Appointment, pk=pk)
    appt.status = "cancelled"
    appt.save()
    messages.success(request, "Appointment cancelled.")
    return redirect("appointments:appointments")


def complete_appointment(request, pk):
    appt = get_object_or_404(Appointment, pk=pk)
    appt.status = "complete"
    appt.save()
    messages.success(request, "Appointment marked complete.")
    return redirect("appointments:appointments")

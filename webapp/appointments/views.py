from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import AppointmentForm
from django.contrib import messages
from .models import Appointment


def welcome(request):
    return render(request, 'welcome.html' , {'greeting': 'Welcome to the site!'})


def appointments(request):
    appointments = Appointment.objects.filter(id = request.user.id)

    return render(request, 'appointments/my_appointments.html' , {'greeting': 'Welcome to the site!', 'appointments': appointments})

def appointment_scheduler(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)  # create but don’t save yet
            appointment.user = request.user        # assign logged-in user
            appointment.save()                     # now save to DB
            messages.success(request, 'Appointment successfully scheduled!')
            return redirect('appointment_scheduler')        # replace with your appointment list page
    else:
        form = AppointmentForm()
    
    return render(request, 'appointments/reserve_slot.html', {'form': form})
 
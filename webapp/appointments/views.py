from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import AppointmentForm
from django.contrib import messages


def welcome(request):
    return render(request, 'welcome.html' , {'greeting': 'Welcome to the site!'})


def appointment(request):
    return HttpResponse("Appointment Test Page")

def appointment_scheduler(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)  # create but don’t save yet
            appointment.user = request.user        # assign logged-in user
            appointment.save()                     # now save to DB
            messages.success(request, 'Appointment successfully scheduled!')
            return redirect('appointment')        # replace with your appointment list page
    else:
        form = AppointmentForm()
    
    return render(request, 'appointment_scheduler.html', {'form': form})

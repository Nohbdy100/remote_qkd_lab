from django.shortcuts import render
from .forms import CameraRotate

def home(request):
    form = CameraRotate()
    context = {'form': form}
    return render(request, 'core/home.html', context)

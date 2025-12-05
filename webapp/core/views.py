from django.shortcuts import render
from .forms import LensPolarity

def home(request):
    form = LensPolarity()
    context = {'form': form}
    return render(request, 'core/home.html', context)

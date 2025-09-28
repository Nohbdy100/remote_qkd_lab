from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def appointment(request):
    return HttpResponse("Hello, world! This is the appointments app.")

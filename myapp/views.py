from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world! This is the home page.")

# Create your views here.

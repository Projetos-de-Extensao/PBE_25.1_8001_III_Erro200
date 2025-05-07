from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # ou 'index.html', dependendo do seu template

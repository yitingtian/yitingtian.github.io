from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'BasePage.html')

def Resume(request):
    return render(request, 'resume.html')
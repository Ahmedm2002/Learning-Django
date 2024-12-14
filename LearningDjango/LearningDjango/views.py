#  Its name must be views.py 

# It is the main controller where logic is writter

# This file has the access to database to perform CURD operations

# Sometimes the view uses templates to send data to Django which then sends it to the Website 

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
  # return HttpResponse('Hello World! Home Page')
  return render(request, 'index.html')

def aboutUs(request):
  return render(request , 'about.html')

def contactUs(request):
  return render(request, 'contact.html')

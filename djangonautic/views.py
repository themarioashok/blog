from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return HttpResponse('<h1>Homepage</h1>')

def about(request):
    return HttpResponse('<h1>About Page</h1>')

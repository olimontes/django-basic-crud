from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Holy Shii")

def about(request):
    return HttpResponse("About page")
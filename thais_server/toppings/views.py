from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Some toppings.")

def blah(request):
    return HttpResponse("Mushrooms.")
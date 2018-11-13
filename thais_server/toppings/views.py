from django.shortcuts import render

from django.http import HttpResponse
from django.template import Context, loader

def index(request):
    return HttpResponse("Some toppings.")

def blah(request):
    return HttpResponse("Mushrooms.")

def zacks_html(request):
    template = loader.get_template("zack.html")
    return HttpResponse(template.render())
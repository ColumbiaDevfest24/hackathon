from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(response):
    return render(response, "main/home.html", {})
def volunteer(response):
    return render(response, "main/volunteer.html", {})
def intercession(response):
    return render(response, "main/intercession.html", {})
def tompkins(response):
    return render(response, "main/tompkins.html", {})
def help(response):
    return render(response, "main/help.html", {})
def calendar(response):
    return render(response, "main/calendar.html", {})


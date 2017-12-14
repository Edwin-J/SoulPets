from django.shortcuts import render
from . import models

def main(request) :
    return render(request, "menu/main.html")

def bombei(request) :
    return render(request, "menu/bombeiPage.html")

def chiwawa(request) :
    return render(request, "menu/chiwawaPage.html")

def cogi(request) :
    return render(request, "menu/cogiPage.html")

def shiam(request) :
    return render(request, "menu/shiamPage.html")

def siva(request) :
    return render(request, "menu/sivaPage.html")

def tabie(request) :
    return render(request, "menu/TabiePage.html")

def bierd(request) :
    return render(request, "menu/BierdPage.html")

def hedge(request) :
    return render(request, "menu/HedgePage.html")

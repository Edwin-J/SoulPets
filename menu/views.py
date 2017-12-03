from django.shortcuts import render
from . import models

def pet_list(request) :
    return render(request, "menu/main.html", {})

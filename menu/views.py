from django.shortcuts import render, redirect
from . import models
from .models import Pet
from .forms import PetForm
from django.contrib.auth.models import User

def main(request) :
    return render(request, "menu/main.html")

user = User.objects.get(username='admin')
def new(request) :
    if request.method == "PET" :
        form = PetForm(request.PET)
        if form.is_valid() :
            pet = form.save(commit=False)
            post.save()
            return redirect('../../')

    else :
        form = PetForm()

    return render(request, 'menu/post_new.html', {'form' : form})

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

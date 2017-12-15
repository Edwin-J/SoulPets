from django.shortcuts import render, redirect, get_object_or_404
from . import models
from .models import Pet, Comment
from .forms import PetForm, CommentForm
from django.contrib.auth.models import User

def main(request) :
    return render(request, "menu/main.html")

user = User.objects.get(username='admin')
def new(request) :
    if request.method == "POST" :
        form = PetForm(request.POST)
        if form.is_valid() :
            pet = form.save(commit=False)
            pet.save()
            return redirect('main')

    else :
        form = PetForm()
        return render(request, 'menu/post_new.html', {'form' : form})

def base(request) :
    pet = get_object_or_404(Pet)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = pet
            comment.save()
            return redirect('main')
    else :
        form = CommentForm()

def bombei(request) :
    return render(request, "menu/bombeiPage.html")

def chiwawa(request) :
    return render(request, "menu/chiwawaPage.html")

def cogi(request) :
    return render(request, "menu/cogiPage.html")

def shiam(request) :
    return render(request, "menu/shiamPage.html")

def siva(request) :
    pet = get_object_or_404(Pet)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = pet
            comment.save()
            return redirect('main')
    else :
        form = CommentForm()

    return render(request, "menu/sivaPage.html", {'form' : form})

def tabie(request) :
    return render(request, "menu/TabiePage.html")

def bierd(request) :
    return render(request, "menu/BierdPage.html")

def hedge(request) :
    return render(request, "menu/HedgePage.html")

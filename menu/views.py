from django.shortcuts import render, redirect, get_object_or_404
from . import models
from .models import Pet, Comment
from .forms import PetForm, CommentForm
from django.utils import timezone
from django.db.models import F

def main(request) :
    pets = Pet.objects.all()
    return render(request, "menu/main.html", {'pets' : pets})

def new(request) :
    if request.method == "POST" :
        form = PetForm(request.POST)
        if form.is_valid() :
            pet = form.save(commit=False)
            pet.published_date = timezone.now()
            pet.save()
            return redirect('menu:main', pk = pet.pk)
    else :
        form = PetForm()
    return render(request, 'menu/post_new.html', {'form' : form})

def detail(request, pk) :
    pet = get_object_or_404(Pet, pk=pk)
    Pet.objects.filter(id = pk).update(hits = F('hits') + 1)
    return render(request, 'menu/post_detail.html', {'pets':pet})

def base(request) :
    pet = get_object_or_404(Pet, pk=pk)
    if request.method == "POST" :
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = pet
            comment.save()
            return redirect('menu:main')
    else :
        form = CommentForm()

def bombei(request) :
    pet=get_object_or_404(Pet,pk=pk)
    if request.method == "POST" :
        form=CommentForm(request.POST)
        if	form.is_valid():
            comment	= form.save(commit=False)
            comment.post=pet
            comment.writer=request.user
            comment.approved_comment=True
            comment.save()
            return	redirect('menu.views.detail', pk=pet.pk)
    else:
        form	=	CommentForm()
        context	=	{"pets":pet,"form":form}
    return	render(request,"menu/bombeipage.html",context)


def chiwawa(request, pk) :
    pet = get_object_or_404(Pet, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = pet
            comment.save()
            return redirect('main')
    else :
        form = CommentForm()


    return render(request, "menu/chiwawaPage.html")

def cogi(request) :
    return render(request, "menu/cogiPage.html")

def shiam(request) :
    return render(request, "menu/shiamPage.html")

def siva(request) :
    return render(request, "menu/sivaPage.html", {'form' : form})

def tabie(request) :
    return render(request, "menu/TabiePage.html")

def bierd(request) :
    return render(request, "menu/BierdPage.html")

def hedge(request) :
    return render(request, "menu/HedgePage.html")

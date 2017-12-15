from django import forms
from .models import Pet, Comment

class PetForm(forms.ModelForm) :
    class Meta :
        model = Pet
        fields = ('title', 'kind', 'price', 'info',)

class CommentForm(forms.ModelForm) :
    class Meta :
        model = Comment
        fields = ('text', )

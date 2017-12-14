from django import forms
from .models import Pet

class PetForm(forms.ModelForm) :
    class Meta :
        model = Pet
        fields = ('title', 'kind', 'price', 'info', 'imgs')

from django import forms
from .models import Community 

class CreateCommunity(forms.ModelForm): 
    class Meta:
        model = Community  
        fields = ['title', 'description', 'slug', 'banner'] 

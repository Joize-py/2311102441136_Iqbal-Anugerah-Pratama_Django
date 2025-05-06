from django import forms
from Character.models import Hero

class HeroForm(forms.ModelForm):
    
    class Meta:
        model = Hero
        fields = ['name', 'role', 'image' ,'tier', 'tier', 'description']

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                    }),


            'role': forms.Select(
                attrs={
                    'class': 'form-control'
                    }),


            'tier': forms.Select(
                attrs={
                    'class': 'form-control'
                    }),


            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 5,
                    'placeholder': 'Description'
                    }),
        }
        
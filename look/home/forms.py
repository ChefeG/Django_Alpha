from django import forms

from .models import Districts, Reviews
from django.forms import TextInput, DateTimeInput, Textarea

class DisctictsForm(forms.ModelForm):
    class Meta:
        model = Districts
        fields = ['image', 'name', 'url', 'metro', 'price', 'description']

class ReviewsForm(forms.ModelForm):
    '''Форма отзывов'''

    class Meta:
        model = Reviews
        fields = ('text', 'name', 'date',)
        # widgets = {
        #     'name': forms.TextInput(attrs={'class':'form-control border', 'placeholder': 'Name'}),
        #     'text': forms.Textarea(attrs={'class':'form-control border', 'placeholder': 'Your review...'})
        # }

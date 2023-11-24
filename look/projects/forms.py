from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField

from .models import Districts, Reviews
from django.forms import TextInput, DateTimeInput, Textarea

class DisctictsForm(forms.ModelForm):
    class Meta:
        model = Districts
        fields = ['image', 'name', 'url', 'metro', 'price', 'description']

class ReviewsForm(forms.ModelForm):
    '''Форма отзывов'''
    captcha = ReCaptchaField()

    class Meta:
        model = Reviews
        fields = ('text', 'name', 'date', 'captcha',)
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control border'}),
            'name': forms.TextInput(attrs={'class': 'form-control border'}),
            'date': forms.DateField(attrs={'class': 'form-control border'}),
        }
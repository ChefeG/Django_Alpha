from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField

from contact.models import Contact


class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Contact
        fields = ('email',)
        widgets = {
            'email': forms.TextInput(attrs={
                'class': 'editContent',
                'placeholder': 'Your Email...'
            })
        }
        labels = {
            'email': ''
        }
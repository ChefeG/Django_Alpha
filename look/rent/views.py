from django.shortcuts import render

from home.models import Category


def rent(request):
    data = Category.objects.all()
    return render(request, 'home/elements.html', {'cat': data} )

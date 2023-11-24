from django.shortcuts import render

from home.models import Category


def support(request):
    data = Category.objects.all()
    return render(request, 'home/index.html', {'cat': data})
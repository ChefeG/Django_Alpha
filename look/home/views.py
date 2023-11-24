from django.shortcuts import render, redirect
# from django.views import View
from django.views.generic import DetailView, ListView
#
# from .forms import ReviewsForm

from .models import Districts, Category, DistrictsNews, DistrictsImage


def home(request):
    category = Category.objects.all()
    district = Districts.objects.all()
    return render(request, 'home/index.html', {'dist': district, 'cat': category})

class Search(ListView):
    context_object_name = 'projects'
    template_name = 'projects/projects.html'
    paginate_by = 2

    def get_queryset(self): # запрос в БД (с необходимыми свойствами)
        return Districts.objects.filter(url__icontains=self.request.GET.get('q'))

    def get_context_data(self, *args, **kwargs): #переменные которые можно использовать в темплейтах, и добавить туда какие-то свои переменные
        context = super(Search, self).get_context_data(*args, **kwargs)
        context['q'] = f'q={self.request.GET.get("q")}&'
        return context












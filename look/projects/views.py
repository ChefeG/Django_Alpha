from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from home.models import Districts, Category, DistrictsNews, DistrictsImage, Reviews
from home.forms import ReviewsForm


class Cat:
    '''категории'''

    def get_category(self):
        return Category.objects.all()


class ProjectsListView(ListView, Cat):
    '''Список проектов'''
    model = Districts
    queryset = Districts.objects.all()
    context_object_name = 'projects'
    template_name = 'projects/projects.html'
    paginate_by = 2 # сколько элементов будет на 1


class DistrictDetailView(DetailView, Cat):
    model = Districts
    template_name = 'home/generic.html'
    context_object_name = 'detail'
    slug_field = 'url'


class DistrictNews(DetailView, Cat):
    model = DistrictsNews
    template_name = 'districts/dist.html'
    context_object_name = 'dist_news'


class DistrictImage(DetailView, Cat):
    model = DistrictsImage
    template_name = 'districts/place.html'
    context_object_name = 'dist_image'


class AddReview(View):
    model = Reviews
    template_name = 'home/generic.html'

    def post(self, request, id):
        '''Отправка отзыва'''
        form = ReviewsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.districts_id = id
            form.save()
            return redirect("projects")




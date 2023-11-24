from django.shortcuts import render
from django.views.generic import DetailView, ListView, View

from home.models import Category, Districts


class Cat:
    '''категории'''

    def get_category(self):
        return Category.objects.all()

class Mortgage(View):

    def get(self, request):
        return render(request, 'mortgage/mortgage.html', {'view': Cat})



class ApplyDetailView(ListView, Cat):
    template_name = 'mortgage/apply.html'
    model = Districts

    def get_context_data(self, **kwargs):
        context = super(ApplyDetailView, self).get_context_data(**kwargs)
        context['dist'] = Districts.objects.all()
        return context




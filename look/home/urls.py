from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.Search.as_view(), name='search'),
]

from django.contrib.flatpages import views
urlpatterns += [
    path('about/', views.flatpage, {'url': '/about/'}, name='about'),
]

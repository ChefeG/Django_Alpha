from django.urls import path
from . import views

urlpatterns = [
    path('', views.trade_in, name='mortgage'),
]
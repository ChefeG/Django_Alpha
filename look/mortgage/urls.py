from django.urls import path
from . import views

urlpatterns = [
    path('', views.Mortgage.as_view(), name='mortgage'),
    path('apply/', views.ApplyDetailView.as_view(), name='apply')
    ]


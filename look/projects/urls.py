from django.urls import path
from . import views

urlpatterns = [
    # Projects
    path('', views.ProjectsListView.as_view(), name='projects'),
    # District
    path('<slug:slug>/', views.DistrictDetailView.as_view(), name='detail'),
    path('news/<int:pk>/', views.DistrictNews.as_view(), name='dist_news'),
    path('image/<slug:slug>/', views.DistrictImage.as_view(), name='dist_image'),
    path('review/<int:id>', views.AddReview.as_view(), name='add_review'),
]

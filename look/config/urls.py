from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'), name='home'),
    path('projects/', include('projects.urls'), name='projects'),
    path('mortgage/', include('mortgage.urls'), name='mortgage'),
    path('rent/', include('rent.urls'), name='rent'),
    path('trade_in/', include('trade_in.urls'), name='trade_in'),
    path('support/', include('support.urls'), name='support'),


    path('contact/', include('contact.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



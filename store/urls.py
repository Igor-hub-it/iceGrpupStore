from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', main, name='main'),
    path('catalog', catalog, name='catalog'),
    path('contacts', contacts, name='contacts')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

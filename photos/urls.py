from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'photos'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('location/<location>\w+)/', views.location, name='location'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
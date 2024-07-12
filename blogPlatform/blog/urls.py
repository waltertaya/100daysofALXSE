from django.urls import path
from .views import index, about

urlpatterns = [
    path('', index, name='blog-home'),
    path('about/', about, name='blog-about')
]

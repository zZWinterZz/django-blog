"""URL patterns for about app."""
from . import views
from django.urls import path

urlpatterns = [
    # About page
    path('', views.about_me, name='about'),
]
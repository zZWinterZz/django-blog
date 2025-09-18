"""URL configuration for codestar project."""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),
    # Blog app
    path("", include("blog.urls"), name="blog-urls"),
    # About app
    path("about/", include("about.urls"), name="about-urls"),
    # Allauth (accounts)
    path("accounts/", include("allauth.urls")),
    # Summernote editor
    path('summernote/', include('django_summernote.urls')),
]

"""URL patterns for blog app."""
from . import views
from django.urls import path

urlpatterns = [
    # Home page: list posts
    path('', views.PostList.as_view(), name='home'),
    # Post detail
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    # Edit comment
    path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    # Delete comment
    path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
]
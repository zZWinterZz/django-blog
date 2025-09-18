"""Models for blog posts and comments."""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
    
STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    """Blog post model."""
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="blog_posts"
)
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        """String representation of Post."""
        return f"{self.title} | written by {self.author}"
    



class Comment(models.Model):
    """Comment model for blog posts."""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        """String representation of Comment."""
        return f"Comment {self.body} | by {self.author}"
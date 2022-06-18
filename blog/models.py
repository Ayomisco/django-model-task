from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    text = models.TextField(verbose_name="Text", help_text="Enter Your test")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Username")
    created_at = models.DateTimeField()
    published_date = models.DateTimeField()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Post"
        verbose_name_plural = "Posts"
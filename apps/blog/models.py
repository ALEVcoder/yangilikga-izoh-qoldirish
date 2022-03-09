from operator import mod
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    """
    Yangiliklar modeli
    """

    title = models.CharField(max_length=256)
    subtitle = models.CharField(max_length=100)
    slug = models.SlugField(max_length=512)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='news')
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])


class Comment(models.Model):
    """
        Izohlar uchun model
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    parent_comment = models.ForeignKey(
        'self', 
        on_delete=models.SET_NULL, 
        related_name='child_commends',
        null=True, blank=True
    )
    content = models.CharField(max_length=2012)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "%sga izoh yozildi" % self.post.title    
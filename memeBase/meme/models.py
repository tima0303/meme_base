from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager


class Meme(models.Model):
    """
    Реализация модели мемов
    """

    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)

    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    favorites = models.ManyToManyField(User, related_name='favourite', default=None, blank=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мем'
        verbose_name_plural = 'Мемы'

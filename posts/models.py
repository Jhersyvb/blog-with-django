from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    comment_count = models.IntegerField(default=0)
    thumbnail = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()

    def __str__(self):
        return self.title

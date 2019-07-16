from django.db import models
from django.utils import timezone


class User(models.Model):

    login = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.login


class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    ip = models.GenericIPAddressField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Rating(models.Model):
    choice = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=choice, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.post.title

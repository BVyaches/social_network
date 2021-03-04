from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    group = models.ForeignKey('Group', on_delete=models.CASCADE, null=True, blank=True)


class Group(models.Model):
    title = models.CharField(max_length=15)
    slug = models.SlugField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.title

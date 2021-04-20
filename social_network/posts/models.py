from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=15, help_text='Введите Название', verbose_name='Название')
    slug = models.SlugField(unique=True)
    description = models.TextField(help_text='Введите Описание', verbose_name='Описание')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(help_text='Введите текст', verbose_name='Текст')
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='posts')
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        null=True,
        blank=True
        )

    def __str__(self):
        return self.text[:15]

    class Meta:
        ordering = ('-pub_date',)

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from users.models import CustomUser


class News(models.Model):
    name = models.CharField(
        verbose_name='Название новости',
        max_length=200
    )
    score = models.IntegerField(
        validators=[MaxValueValidator(10), MinValueValidator(1)]
    )
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='news')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField('Текст комментария')
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='author')
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.text

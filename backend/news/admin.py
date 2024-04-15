from django.contrib.admin import ModelAdmin, register

from .models import News, Comment


@register(News)
class NewsAdmin(ModelAdmin):
    list_display = ('name', 'author',)
    list_filter = ('name', 'author',)


@register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = ('author',)
    list_filter = ('author',)

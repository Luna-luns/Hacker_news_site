from django.db.models import Avg
from news.models import News


def get_all_news() -> News:
    """Возвращает список всех новостей c рейтингом."""

    return News.objects.all().annotate(rating=Avg('news__score'))

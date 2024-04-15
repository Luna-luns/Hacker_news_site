from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import NewsViewSet, CommentViewSet

router = DefaultRouter()

router.register(r'news', NewsViewSet, basename='news')
router.register(r'news/(?P<news_id>\d+)/comments',
                CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
]

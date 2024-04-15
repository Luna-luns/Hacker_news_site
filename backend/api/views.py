from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from news.models import News, Comment
from users.models import CustomUser
from .serializers import NewsSerializer, CommentSerializer, CustomUserSerializer


class NewsViewSet(viewsets.ModelViewSet):
    """Обрабатывает новости."""
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Обрабатывает комментарии."""
    serializer_class = CommentSerializer

    def get_queryset(self):
        news_id = self.kwargs.get('news_id')
        news = get_object_or_404(NewsViewSet, pk=news_id)
        new_queryset = news.comments.all()
        return new_queryset

    def perform_create(self, serializer):
        news_id = self.kwargs.get('news_id')
        news = get_object_or_404(News, pk=news_id)
        serializer.save(author=self.request.user, post=news)


class CustomUserViewSet(viewsets.ModelViewSet):
    """Обрабатывает пользователей."""

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (AllowAny,)

    @action(
        methods=['get'],
        detail=False,
        url_path='me',
        url_name='me',
        permission_classes=(IsAuthenticated,)
    )
    def get_me(self, request):
        serializer = CustomUserSerializer(
            request.user,
            context={"request": self.request}
        )

        return Response(serializer.data, status.HTTP_200_OK)

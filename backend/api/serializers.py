from rest_framework import serializers

from news.models import News, Comment
from users.models import CustomUser


class NewsSerializer(serializers.ModelSerializer):
    """Обработчик новостей."""

    rating = serializers.IntegerField()

    class Meta:
        model = News
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """Обработка комментария."""

    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date',)
        read_only_fields = ('id', 'author', 'pub_date',)


class UsernameValidateSerializer:
    """Обработчик проверяет поле username на различие с me."""

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                'Запрещено использовать зарезервированные имена.')

        return value


class CustomUserSerializer(UsernameValidateSerializer):
    """Обработчик пользователей."""

    class Meta:
        model = CustomUser
        fields = (
            'id',
            'email',
            'username',
            'first_name',
            'last_name'
        )

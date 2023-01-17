from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# добавить недостающие модели в приложении posts
class Group(models.Model):
    title = models.CharField(
        'Title',
        max_length=settings.CHAR_IN_GROUP
    )
    slug = models.SlugField(
        max_length=settings.CHAR_IN_SLUG_GROUP,
        unique=True
    )
    description = models.TextField(
        'Description',
        null=False,
        blank=False
    )

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )
    image = models.ImageField(
        upload_to='posts/',
        null=True,
        blank=True
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name="posts",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )

# в проекте должна быть описана модель Follow,
# в ней должно быть два поля —
# user (кто подписан)
# и following (на кого подписан).


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Блогер'
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='uniq_follow'
            ),
        )

    def __str__(self):
        return f'{self.user}'

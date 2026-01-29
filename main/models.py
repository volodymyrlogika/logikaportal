from django.db import models
from django.contrib.auth.models import User


class ForumTopic(models.Model):
    title = models.CharField(max_length=200)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='forum_topics'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ForumPost(models.Model):
    topic = models.ForeignKey(
        ForumTopic,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='forum_posts'
    )
    content = models.TextField()
    image = models.ImageField(upload_to='forum_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username}: {self.content[:30]}'


class Reaction(models.Model):
    REACTION_CHOICES = [
        ('like', '👍'),
        ('dislike', '👎'),
        ('love', '❤️'),
        ('funny', '😂'),
        ('angry', '😠'),
        ('sad', '😢'),
        ('wow', '😮'),
        ('confused', '😕'),
        ('surprised', '😲'),
    ]

    post = models.ForeignKey(
        ForumPost,
        on_delete=models.CASCADE,
        related_name='reactions'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='forum_reactions'
    )
    reaction_type = models.CharField(max_length=10, choices=REACTION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user', 'reaction_type')


class Comment(models.Model):
    post = models.ForeignKey(
        ForumPost,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='forum_comments'
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class CommentReaction(models.Model):
    REACTION_CHOICES = [
        ('like', '👍'),
        ('dislike', '👎'),
        ('love', '❤️'),
    ]

    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name='reactions'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    reaction_type = models.CharField(max_length=10, choices=REACTION_CHOICES)

    class Meta:
        unique_together = ('comment', 'user', 'reaction_type')

from django.db import models

# Create your models here.
class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='announcements/', blank=True, null=True)
    status = models.CharField(max_length=50, default='draft', choices=[('draft', 'Чернетка'), ('published', 'Опубліковано')])

    def __str__(self):
        return self.title
    
from django.db import models

# Create your models here.
class Announcement(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')
    author = models.CharField(max_length=100, verbose_name='Автор')
    image = models.ImageField(upload_to='announcements/', blank=True, null=True, verbose_name='Зображення')
    status = models.CharField(max_length=50, default='draft', choices=[('draft', 'Чернетка'), ('published', 'Опубліковано')], verbose_name='Статус')

    def __str__(self):
        return self.title
    
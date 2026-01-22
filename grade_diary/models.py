from django.db import models
from django.contrib.auth.models import User

# Create your models here. 
class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='Назва уроку')
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Вчитель')
    date_time = models.DateTimeField(verbose_name='Дата і час проведення')
    description = models.TextField(blank=True, null=True, verbose_name='Опис уроку')

    def __str__(self):
        return self.name
    
class Grade(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Учень')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Урок')
    score = models.IntegerField(verbose_name='Оцінка')
    date_recorded = models.DateTimeField(auto_now_add=True, verbose_name='Дата запису оцінки')
    comment = models.TextField(blank=True, null=True, verbose_name='Коментарі')

    def __str__(self):
        return f'{self.student.username} - {self.lesson.name}: {self.score}'
    
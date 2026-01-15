from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="profile") #user
    avatar = models.ImageField(upload_to=''' папка з pfp ''', blank=True, null=True) #pfp
    bio = models.TextField(max_length=1000, blank=True) #bio
    location = models.CharField(max_length=100, blank=True) #локація користувача 
    website = models.URLField(blank=True) #особистий сайт користувача (якщо є)
    created_at = models.DateTimeField(auto_now_add=True) #account_creation_date

    def __str__(self):
        return f"Profile of {self.user.username}"


class Skill(models.Model): #навички користувача
   
    name = models.CharField(max_length=100) #назва навички (наприклад: Python, Django)
    level = models.PositiveSmallIntegerField(help_text="Рівень від 1 до 10") #рівень володіння навичкою
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="skills") #зв’язок навички з профілем користувача

    def __str__(self):
        return f"{self.name} ({self.level}/10)"


class Project(models.Model):  #модель проєктів портфоліо
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="projects") #профіль, якому належить проєкт
    title = models.CharField(max_length=200) #назва проєкту
    description = models.TextField()  #опис проєкту
    link = models.URLField(blank=True) #посилання на проєкт (GitHub, сайт)
    image = models.ImageField(upload_to=''' папка зі скріншотами проєкту ''', blank=True, null=True) #зображення / скріншот проєкту
    created_at = models.DateTimeField(auto_now_add=True) #дата додавання проєкту

    def __str__(self):
        return self.title


class SocialLink(models.Model): #соціальні мережі / зовнішні посилання

    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="social_links") #профіль користувача
    name = models.CharField(max_length=50, help_text="Напр. GitHub, LinkedIn") #назва соцмережі
    url = models.URLField() #URL посилання

    def __str__(self):
        return f"{self.name} - {self.profile.user.username}"

from django.contrib import admin
from .models import ForumPost, ForumTopic, Comment

# Register your models here.
admin.site.register(ForumPost)
admin.site.register(ForumTopic)
admin.site.register(Comment)

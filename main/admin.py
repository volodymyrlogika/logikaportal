from django.contrib import admin
from .models import ForumPost, ForumTopic

# Register your models here.
admin.site.register(ForumPost)
admin.site.register(ForumTopic)
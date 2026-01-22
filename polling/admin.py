from django.contrib import admin
from .models import Polling, Choice

admin.site.register(Polling)
admin.site.register(Choice)

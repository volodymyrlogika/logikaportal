from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from main.models import ForumTopic

# Create your views here.
class TopicListView(LoginRequiredMixin,ListView):
    model = ForumTopic
    template_name = 'topic_list.html'
    context_object_name = 'topic_list'
    ordering = ['-created_at']
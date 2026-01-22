from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Announcement

class AnnouncementListView (ListView):
    model = Announcement
    template_name = 'announcement/announcement_list.html'
    context_object_name = 'announcements'

class AnnouncementDetailView (DetailView):
    model = Announcement
    template_name = 'announcement/announcement_detail.html'
    context_object_name = 'announcement'
    

class AnnouncementCreateView(CreateView):
    model = Announcement
    template_name = 'announcement/announcement_form.html'
    fields = ['title', 'content', 'author', 'image', 'status']
    success_url = '/announcements/list/'  
from django.shortcuts import render
from django.views.generic import ListView
from .models import Announcement
# Create your views here.
class AnnouncementListView (ListView):
    model = Announcement
    template_name = 'announcement_list.html'
    context_object_name = 'announcements'
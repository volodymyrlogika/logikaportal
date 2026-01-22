from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .models import Polling, Choice
from django.views.generic import ListView, DetailView


class PollingListView(ListView):
    model = Polling
    template_name = 'polling_list.html'
    context_object_name = 'polling_list'
    ordering = ['created_at']

class PollingDetailView(DetailView):
    model = Polling
    template_name = 'polling/polling_detail.html'
    context_object_name = 'polling'
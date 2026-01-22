from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.TopicListView.as_view(), name='topic_list'),
    path('topic/<int:topic_id>/', views.topic_detail, name='topic_detail'),
]


from django.urls import path
from .views import TopicListView, topic_detail

urlpatterns = [
    path('', TopicListView.as_view(), name='topic_list'),
    path('topic/<int:topic_id>/', topic_detail, name='topic_detail'),
]

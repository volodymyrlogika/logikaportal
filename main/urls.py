from django.urls import path
from .views import TopicListView, topic_detail
from .views import delete_comment


urlpatterns = [
    path('', TopicListView.as_view(), name='topic_list'),
    path('topic/<int:topic_id>/', topic_detail, name='topic_detail'),
    path('comment/delete/<int:comment_id>/', delete_comment, name='delete_comment'),

]

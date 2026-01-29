from django.urls import path
from django.contrib.auth import views as auth_views
from .views import TopicListView, topic_detail, delete_comment

urlpatterns = [
    path('', TopicListView.as_view(), name='topic_list'),
    path('topic/<int:topic_id>/', topic_detail, name='topic_detail'),
    path('comment/delete/<int:comment_id>/', delete_comment, name='delete_comment'),

    # Login/Logout
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]

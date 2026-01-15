from django.urls import path
from . import views

urlpatterns = [
    path('', views.TopicListView.as_view() , name='views.'),
    
]




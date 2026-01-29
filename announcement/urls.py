from django.urls import path
from . import views

urlpatterns = [

    
    
    path('list/', views.AnnouncementListView.as_view(), name='announcement_list'),
    path('<int:pk>/', views.AnnouncementDetailView.as_view(), name='announcement_detail'),
    path('form/', views.AnnouncementCreateView.as_view(), name='announcement_form'),
]
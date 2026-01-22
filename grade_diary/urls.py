from django.urls import path
from . import views

urlpatterns = [
    # Визнач тут свої URL-шляхи
    path('', views.grade_diary_home, name='grade_diary_home'),
]
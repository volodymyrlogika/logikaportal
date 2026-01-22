from django.urls import path
from .import views

urlpatterns = [
    # перегляд профілю
    path("profile/edit/", views.profile_edit, name="profile_edit"),
    
    # редагування профілю
    path("profile/<str:username>/", views.profile_detail, name="profile_detail"),

    # навички
    path("skills/add/", views.skill_add, name="skill_add"),
    path("skills/<int:pk>/edit/", views.skill_edit, name="skill_edit"),
    path("skills/<int:pk>/delete/", views.skill_delete, name="skill_delete"),

    # проєкти
    path("projects/add/", views.project_add, name="project_add"),
    path("projects/<int:pk>/", views.project_detail, name="project_detail"),
    path("projects/<int:pk>/edit/", views.project_edit, name="project_edit"),
    path("projects/<int:pk>/delete/", views.project_delete, name="project_delete"),
]

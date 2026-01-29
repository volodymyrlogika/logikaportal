from django.urls import path
from . import views

urlpatterns = [
    path("", views.PollingListView.as_view(), name="polling_list"),
    path("<int:pk>/", views.PollingDetailView.as_view(), name="polling_detail"),
]
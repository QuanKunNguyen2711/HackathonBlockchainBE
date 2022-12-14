from django.urls import path
from Projects.views import post_project

urlpatterns = [
    path('post_project', post_project),
]
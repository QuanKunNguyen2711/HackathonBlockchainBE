from django.urls import path
from Projects.views import post_project, get_detail, list_projects

urlpatterns = [
    path('post_project', post_project),
    path('get_detail', get_detail),
    path('list_projects', list_projects)
]
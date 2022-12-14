from django.urls import path
from UserManager.views import login, update_profile

urlpatterns = [
    path('login', login),
    path('update_profile', update_profile)
]
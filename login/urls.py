from django.urls import include, path
from .views import authView, home

urlpatterns = [
    path("", home, name='home'),
    path("signup/", authView, name='authView'),
    path("accounts/", include("django.contrib.auth.urls")),
]
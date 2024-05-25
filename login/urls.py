from django.urls import include, path
from .views import authView, LoginView, dashboard

urlpatterns = [
    path("dashboard/", dashboard, name='dashboard'), # URL for Dashboard
    path("", LoginView.as_view(), name='login'), # Root URL for login
    path("signup/", authView, name='authView'),
    path("accounts/", include("django.contrib.auth.urls")),
]
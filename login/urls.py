from django.urls import include, path
from .views import authView, LoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path("dashboard/", dashboard, name='dashboard'), # URL for Dashboard
    path("", LoginView.as_view(), name='login'), # Root URL for login
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path("signup/", authView, name='authView'),
    path("accounts/", include("django.contrib.auth.urls")),
]
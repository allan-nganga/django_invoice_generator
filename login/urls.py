from django.urls import include, path
from django.contrib.auth import views as auth_views
from .views import login

urlpatterns = [
    # path("dashboard/", dashboard, name='dashboard'), # URL for Dashboard
    #path("", auth_views.LoginView.as_view(template_name='login/login.html'), name='login'), # Root URL for login
    path('', login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    #path("signup/", authView, name='authView'),
    path("accounts/", include("django.contrib.auth.urls")),
]
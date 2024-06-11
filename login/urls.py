from django.urls import include, path
from .views import login_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path("dashboard/", dashboard, name='dashboard'), # URL for Dashboard
    #path("", auth_views.LoginView.as_view(template_name='login/login.html'), name='login'), # Root URL for login
    path('', login_view, name='login_view'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    #path("signup/", authView, name='authView'),
    path("accounts/", include("django.contrib.auth.urls")),
]
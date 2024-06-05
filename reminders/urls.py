from django.urls import path
from . import views

app_name = 'reminders'

urlpatterns = [
    path('', views.reminder_list, name='reminder_list'),
    path('<int:reminder_id>/', views.reminder_detail, name='reminder_detail'),
    path('create/', views.reminder_create, name='reminder_create'),
    path('<int:reminder_id>/edit/', views.reminder_edit, name='reminder_edit'),
    path('<int:reminder_id>/delete/', views.reminder_delete, name='reminder_delete'),
]
from django.urls import path
from . import views

app_name = 'password_dashboard'

urlpatterns = [
    path('',views.PasswordDashboardView,name="password_dashboard"),
]
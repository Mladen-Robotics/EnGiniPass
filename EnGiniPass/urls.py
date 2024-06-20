from django.contrib import admin
from django.urls import path,include
from user_authentication import views as auth_views

app_name = "EnGiniPass"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',auth_views.LoginView,name="login"),
    path('signup/',auth_views.SignupView,name="signup"),
    path('logout/',auth_views.LogoutView,name="logout"),
    path('dashboard/',include("password_dashboard.urls")),
    path('',auth_views.HomePageView,name="home"),
]

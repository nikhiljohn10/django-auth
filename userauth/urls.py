from django.urls import path
from userauth import views

urlpatterns = [
    path('', views.home, name="home"),
    path('profile/', views.user_profile, name='profile'),
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]

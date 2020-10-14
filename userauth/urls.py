from django.urls import path
from userauth import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup_user, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
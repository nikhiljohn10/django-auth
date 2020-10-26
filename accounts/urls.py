from django.urls import path
from accounts import views

app_name = 'auth'
urlpatterns = [
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('enable/<username>', views.user_enable, name='enable'),
    path('disable/<username>', views.user_disable, name='disable'),
    path('delete/<username>', views.user_delete, name='delete'),
]

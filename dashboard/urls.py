from django.urls import path
from dashboard import views

app_name = 'dash'
urlpatterns = [
    path('', views.home, name="home"),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
    path('profile/disable', views.profile_disable, name='profile_disable'),
    path('profile/delete', views.profile_delete, name='profile_delete'),
]

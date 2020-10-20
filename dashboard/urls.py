from django.urls import path
from dashboard import views

app_name = 'dash'
urlpatterns = [
    path('', views.home, name="home"),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.ProfileEditView.as_view(), name='profile_edit'),
]

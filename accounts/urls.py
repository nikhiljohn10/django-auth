from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import RedirectView
from accounts import views

urlpatterns = [
	path('', RedirectView.as_view(url='/accounts/profile/')),
	path('login/', LoginView.as_view(template_name='auth/user_login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/', views.user_profile, name='profile'),
    path('profile/edit/', views.ProfileEditView.as_view(), name='profile_edit'),
	path('device/', views.user_device, name='device'),
	path('device/new/', views.TOTPCreateView.as_view(), name='create_device'),
    path('device/qrcode/', include('qr_code.urls', namespace="qr_code")),
]

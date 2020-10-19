from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/dashboard/')),
    path('dashboard/', include('dashboard.urls', namespace='dash')),
    path('auth/', include('accounts.urls', namespace='auth')),
    path('admin/', admin.site.urls),
]

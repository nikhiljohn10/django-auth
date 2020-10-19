from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from accounts.views import dashboard

urlpatterns = [
	path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard, name='dashboard'),
]

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', include('core.urls', namespace='core')),
    path('dashboard/', include('dashboard.urls', namespace='dash')),
    path('auth/', include('accounts.urls', namespace='auth')),
    path('admin/', admin.site.urls),
]

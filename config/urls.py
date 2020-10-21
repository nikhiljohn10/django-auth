from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf.urls.static import static

urlpatterns = [
    path('', include('core.urls', namespace='core')),
    path('dashboard/', include('dashboard.urls', namespace='dash')),
    path('auth/', include('accounts.urls', namespace='auth')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

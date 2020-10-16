from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/auth/')),
    path('auth/', include('userauth.urls')),
    path('admin/', admin.site.urls),
]

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from tracker import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

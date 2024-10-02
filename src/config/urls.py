from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from apps import urls as apps_urls

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('', include(apps_urls)),
    path("summernote/", include("django_summernote.urls")),  # add this
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

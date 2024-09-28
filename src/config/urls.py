from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from apps import urls as apps_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(apps_urls)),
]

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from apps import urls as apps_urls
from apps.views import message, MainView

urlpatterns = [
                  path('api/admin/', admin.site.urls),
                  path('', include(apps_urls)),
                  path('message/', message, name='message'),
                  path("summernote/", include("django_summernote.urls")),  # add this
                  path("Ikamezukashi/", MainView.as_view(), name='Ikamezukashi'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)

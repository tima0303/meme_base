from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from memeSite.views import *

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('memeSite.urls')),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('accounts/', include('accounts.urls')),
                  path('meme/', include('meme.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound

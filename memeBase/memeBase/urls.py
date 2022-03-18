from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from memeBase import settings
from memeSite.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('memeSite.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = pageNotFound

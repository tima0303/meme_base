from django.urls import path

from .views import *

urlpatterns = [
    path('manage/', manage, name='manage'),
    path('bookmarks/', bookmarks, name='bookmarks'),
]
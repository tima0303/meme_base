from django.urls import path

from .views import *


urlpatterns = [
    path('manage/', manage, name='manage'),
    path('bookmarks/', bookmarks, name='bookmarks'),
    path('create/', create, name='create'),
    path('<int:pk>', MemeDetailView.as_view(), name='meme-detail')
]
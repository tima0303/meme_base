from django.urls import path

from .views import *


urlpatterns = [
    path('manage/', manage, name='manage'),
    path('create/', create, name='create'),
    path('<int:id>', meme_detail_view, name='meme-detail')
]
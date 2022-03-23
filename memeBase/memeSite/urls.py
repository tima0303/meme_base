from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('guide/', guide, name='guide'),
    path('user_authorization/', user_authorization, name='user_authorization'),
]

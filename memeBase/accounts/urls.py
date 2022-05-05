from django.urls import path

from .views import *


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('authorization/', authorization, name='authorization'),
    path('personal/', personal, name='personal'),
    path('settings/', settings, name='settings'),
    path('fav/<int:id>/', favorites_add, name='favorite_add'),
    path('favorites/', favorites_list, name='bookmarks'),
]
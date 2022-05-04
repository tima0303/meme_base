from django.urls import path

from .views import *

urlpatterns = [
    path('', MemeHome.as_view(), name='home'),
    path('guide/', guide, name='guide'),
    path('search/', SearchResultView.as_view(), name='search_results')
]

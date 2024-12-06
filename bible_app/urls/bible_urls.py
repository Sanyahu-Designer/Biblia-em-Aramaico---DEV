"""URLs for main Bible navigation."""
from django.urls import path
from ..views.bible_views import home, get_chapters

urlpatterns = [
    path('', home, name='home'),
    path('get-chapters/', get_chapters, name='get_chapters'),
]
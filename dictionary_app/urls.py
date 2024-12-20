from django.urls import path
from .views import home

app_name = 'dictionary_app'

urlpatterns = [
    path('', home, name='home'),
]

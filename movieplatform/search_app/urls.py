from django.urls import path
from . import views

app_name = 'search_app'

urlpatterns = [
    path('', views.movie_search, name='SearchResult'),
]

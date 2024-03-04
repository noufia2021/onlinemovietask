from . import views
from django.urls import path

app_name = 'movie_app'

urlpatterns = [
    path('', views.index, name='index'),
   # path('category_list/',views.category_list,name='category_list'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('category_movies/<int:category_id>/', views.category_movies, name='category_movies'),
    path('add/', views.add_movie, name='add_movie'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),

    #path('movielist/',views.movielist,name='movie_list')
]

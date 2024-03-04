from django.shortcuts import render
from movie_app.models import Category_movie, Movie
from django.db.models import Q

def movie_search(request):
    movies = None
    query = None

    if 'q' in request.GET:
        query = request.GET.get('q')
        movies = Movie.objects.filter(Q(title__icontains=query) | Q(category__title__icontains=query))
        return render(request, 'movie_search.html', {'query': query, 'movies': movies})



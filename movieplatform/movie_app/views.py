from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404


from .models import Category_movie, Movie
from .forms import MovieForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden


# Create your views here.
def index(request):
    movies = Movie.objects.all()
    return render(request, "home.html", {'movies': movies})


def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'detail.html', {'movie': movie})


def category_movies(request, category_id=None):
    category = None
    movies = None

    if category_id is not None:
        category = get_object_or_404(Category_movie, id=category_id)
        movies = Movie.objects.filter(category=category)

    return render(request, 'trial.html', {'category': category, 'movies': movies})


# def category_list(request):
#    categories = Category_movie.objects.all()
#    selected_category = None
#    movies = None

#   if request.method == 'GET' and 'category_id' in request.GET:
#        category_id = request.GET['category_id']
#        if category_id:
#            selected_category = get_object_or_404(Category_movie, id=category_id)
#            movies = selected_category.movie_set.all()

#    return render(request, 'trial.html', {'categories': categories, 'selected_category': selected_category, 'movies': movies})


# def category_list(request):
#    categories = Category_movie.objects.all()
#    return render(request,  "trial.html", {'categories': categories})


@login_required
def add_movie(request):
    if request.method == "POST":
        title = request.POST.get('title_h', )
        poster = request.FILES['poster_h']
        description = request.POST.get('description_h', )
        release_date = request.POST.get('release_date_h', )
        actors = request.POST.get('actors_h', )
        category_id = request.POST.get('category_h', )
        trailer_link = request.POST.get('trailer_link_h', )

        if category_id == 'Choose category' or category_id is None:
            messages.info(request, "Select category!")
            return redirect('movie_app:add_movie')

        category = Category_movie.objects.get(id=category_id)

        movie = Movie(
            title=title, poster=poster, description=description,
            release_date=release_date, actors=actors, category=category,
            trailer_link=trailer_link, added_by=request.user
        )
        movie.save()

    categories = Category_movie.objects.all()
    return render(request, "addmovie.html", {'categories': categories})


def update(request, id):
    # Retrieve the movie instance
    movie = get_object_or_404(Movie, id=id)

    # Check if the user trying to update the movie is the same user who added it
    if request.user == movie.added_by:
        if request.method == 'POST':
            form = MovieForm(request.POST, request.FILES, instance=movie)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            # Initialize the form with the existing movie details
            form = MovieForm(instance=movie)

        return render(request, 'edit.html', {'form': form, 'movie': movie})
    else:
        return render(request,'permission_denied.html')

def delete(request, id):
    movie = get_object_or_404(Movie, id=id)

    # Check if the user trying to delete the movie is the same user who added it
    if request.user == movie.added_by:
        if request.method == 'POST':
            movie.delete()
            return redirect('/')
        return render(request, 'delete.html')
    else:
        return render(request,'permission_denied.html')


# def movielist(request):
#    movies=Movie.objects.all()
#    return render(request,'home.html',{'movies':movies})

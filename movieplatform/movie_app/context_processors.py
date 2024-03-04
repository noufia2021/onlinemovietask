from .models import Category_movie

def menu_links(request):
    links=Category_movie.objects.all()
    return dict(links=links)

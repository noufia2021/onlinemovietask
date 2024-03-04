from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse



# Create your models here.
class Category_movie(models.Model):
    title = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('movie_app:category_movies', args=[str(self.id)])

    def __str__(self):
        return '{}'.format(self.title)



class Movie(models.Model):
    title = models.CharField(max_length=250, unique=True)
    poster = models.ImageField(upload_to='gallery', blank=True)
    description = models.TextField(blank=True)
    release_date = models.DateField()
    actors = models.CharField(max_length=250)
    category = models.ForeignKey(Category_movie, on_delete=models.CASCADE)
    trailer_link = models.URLField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


    class Meta:
        ordering = ('title',)
        verbose_name = 'movie'
        verbose_name_plural = 'movies'

    def __str__(self):
        return '{}'.format(self.title)



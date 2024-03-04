from django.contrib import admin
from .models import Category_movie, Movie


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Category_movie,CategoryAdmin)

class MovieAdmin(admin.ModelAdmin):
    list_display = ['title','release_date','actors','category']
    list_editable = ['actors','category']

    list_per_page = 20
admin.site.register(Movie,MovieAdmin)




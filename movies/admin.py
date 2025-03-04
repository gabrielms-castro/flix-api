from django.contrib import admin

from movies.models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name', 
        'genre',
        'release_date',
        'rating', 
        'resume', 
    )

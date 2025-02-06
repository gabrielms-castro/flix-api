from django.db import models

from actors.models import Actor
from genres.models import Genre

class Movie(models.Model):
    name = models.CharField(max_length=500)
    genre = models.ForeignKey( # ligação 1-to-n
        Genre,
        on_delete=models.PROTECT,
        related_name="movies"
    )
    release_date = models.DateField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    actors = models.ManyToManyField(
        Actor,
        related_name="movies"
    ) # um filme pode ter vários atores n-to-n
    resume = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name
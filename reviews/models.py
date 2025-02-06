from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from movies.models import Movie

class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.PROTECT,
        related_name="reviews"
    )
    stars = models.IntegerField(
        validators=[
            MinValueValidator(1, "Avaliação deve conter no mínimo 1 estrela."),
            MaxValueValidator(5, "Avaliação não pode ser maior que 5 estrelas.")
        ]
    )
    comment = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.movie}"
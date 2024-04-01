from django.db import models
from django.contrib.postgres.fields import ArrayField


class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    genre = ArrayField(models.CharField(max_length=100))
    director = models.CharField(max_length=100)
    cast = ArrayField(models.CharField(max_length=100))
    plot = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    poster = models.ImageField(
                                default='api/static/api/images/posters/default_poster.jpg', 
                                upload_to='api/static/api/images/posters/', 
                                blank=True
                            )

    def __str__(self):
        return self.title

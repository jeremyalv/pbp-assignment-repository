from statistics import mode
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class MyWatchList(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=255)
    rating = models.FloatField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
    ])
    release_date = models.CharField(max_length=10)
    review = models.TextField()
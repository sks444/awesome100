from django.db import models


class TvShow(models.Model):
    rank = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300, null=True)
    url = models.URLField(null=True)
    summary = models.TextField(null=True)
    image_url = models.URLField(null=True)
    rating = models.FloatField(null=True)
    year_of_release = models.CharField(max_length=100, null=True)
    genre = models.TextField(null=True)
    duration = models.CharField(max_length=100, null=True)
    actors_and_directors = models.TextField(null=True)
    votes_and_gross = models.TextField(null=True)
    other_info = models.TextField(null=True)

    def __str__(self):
        return self.name

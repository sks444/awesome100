from django.db import models


class Actor(models.Model):
    rank = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300, null=True)
    url = models.URLField(null=True)
    image_url = models.URLField(null=True)
    summary = models.TextField(null=True)
    best_movie = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name

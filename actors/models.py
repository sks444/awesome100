from django.db import models

class Actor(models.Model):
	rank = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=300)
	url = models.URLField()
	summary = models.TextField()

	def __str__(self):
		return self.name

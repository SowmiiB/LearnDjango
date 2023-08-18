from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length= 200)
    language = models.CharField(max_length= 200)
    poster  = models.ImageField(upload_to='pics')
    rating = models.FloatField()
    ticket_cost = models.FloatField()


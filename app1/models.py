from django.db import models

# Create your models here.

class user(models.Model):
    name =  models.CharField(max_length=30)
    email = models.CharField(max_length = 20)
    password = models.CharField(max_length = 15)

class movie(models.Model):
    movie_name = models.CharField(max_length=30)
    movie_description = models.CharField(max_length=100)
    movie_director = models.CharField(max_length=30)
    movie_duration = models.CharField(max_length=30)
    
class ticket(models.Model):
    ticket_of_movie = models.ForeignKey(movie,on_delete=models.CASCADE)
    timing  = models.CharField(max_length=10)
    price = models.FloatField()
    no_of_ticket = models.IntegerField()
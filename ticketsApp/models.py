from django.db import models

#Customer---Movie---Reservation

class Customer(models.Model):
    name = models.CharField(max_length=20)
    mobile = models.CharField(max_length=15)

class Movie(models.Model):
    hall = models.CharField(max_length=20)
    movie = models.CharField(max_length=50)

class Reservation(models.Model):

    customer = models.ForeignKey(Customer, related_name='reservation', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='reservation', on_delete=models.CASCADE)

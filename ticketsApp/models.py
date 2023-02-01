from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

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

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

from django.contrib import admin
from .models import Customer
from .models import Movie
from .models import Reservation

# Register your models here.
admin.site.register(Customer)
admin.site.register(Movie)
admin.site.register(Reservation)

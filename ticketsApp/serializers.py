from rest_framework import serializers
from ticketsApp.models import Customer, Movie, Reservation

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class CustpmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['pk', 'reservation', 'name', 'mobile']
from django.shortcuts import render
from django.http.response import  JsonResponse
from .models import Customer, Movie, Reservation

# Create your views here.

#1 without REST and no model query(static)
def no_rest_no_model(request):
    customer = [{
        'id':1,
        'Name':'Jack',
        'mobile':'514-578-0298'
    },
        {
            'id': 2,
            'Name': 'John',
            'mobile': '514-598-0299'
        }
    ]
    return JsonResponse(customer, safe=False)

#2 With model data default Django and with no Rest-Framework
def no_rest_with_model(request):
    data = Customer.objects.all()
    response = {
        'customers': list(data.values('name', 'mobile'))
    }
    return JsonResponse(response)


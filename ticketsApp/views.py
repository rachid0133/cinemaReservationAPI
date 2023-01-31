from django.shortcuts import render
from django.http.response import  JsonResponse

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

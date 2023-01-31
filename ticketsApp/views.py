from django.http.response import  JsonResponse
from .models import Customer, Movie, Reservation
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, filters
from .serializers import CustomerSerializer, MovieSerializer, ReservationSerializer

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

#3 Function Based View(FBV) with Rest_Framework
#3.1 GET POST
@api_view(['GET', 'POST'])
def Fbv_list(request):
    #GET
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
    #POST
    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


# 3.2 GET PUT DELETE
@api_view(['GET','PUT','DELETE'])
def Fbv_Put_Delete(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #GET
    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    #PUT
    elif request.method == 'PUT':
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #DELETE
    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
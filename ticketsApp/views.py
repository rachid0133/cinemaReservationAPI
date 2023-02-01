from django.core.exceptions import ObjectDoesNotExist
from django.http.response import JsonResponse, Http404
from .models import Customer, Movie, Reservation
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, filters, generics, mixins, viewsets
from rest_framework.views import APIView
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

#3 Function Based Views(FBV) with Rest_Framework
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
    except ObjectDoesNotExist:
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

#4 Class Based Views(CBV) with Rest_Framework
#4.1 GET POST
class Cbv_list(APIView):
    #GET
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
    #POST
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

#4.2 GET PUT DELETE class based views -- pk
class Cbv_list_pk(APIView):
    #GET
    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except ObjectDoesNotExist:
            raise Http404

    def get(self, request, pk):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    #PUT
    def put(self, request, pk):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #DELETE
    def delete(self, request, pk):
        customer = self.get_object(pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#5 Mixins
#5.1 mixins list GET POST
class mixins_list(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request):
        return self.list(request)
    def post(self, request):
        return self.create(request)
#5.2 mixins get put delete
class mixins_pk(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request, pk):
        return self.retrieve(request)
    def put(self, request, pk):
        return self.update(request)
    def delete(self, request, pk):
        return self.destroy(request)

#6 Generics
#6.1 Get POST
class generics_list(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

#6.2 GET PUT DELETE
class generics_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


#7 viewsets
class viewsets_customer(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class viewsets_movie(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['movie']

class viewsets_reservation(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

#8 find movie
@api_view(['GET'])
def find_movie(request):
    movies = Movie.objects.filter(movie=request.data['movie'])
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

#9 create new reservation
@api_view(['POST'])
def new_reservation(request):
    movie = Movie.objects.get(hall=request.data['hall'], movie=request.data['movie'])

    customer = Customer()
    customer.name = request.data['name']
    customer.mobile = request.data['mobile']
    customer.save()

    reservation = Reservation()
    reservation.customer = customer
    reservation.movie = movie
    reservation.save()

    return Response(status=status.HTTP_201_CREATED)




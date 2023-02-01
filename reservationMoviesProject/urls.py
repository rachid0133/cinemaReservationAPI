from django.contrib import admin
from django.urls import path, include
from ticketsApp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('customers', views.viewsets_customer)
router.register('movies', views.viewsets_movie)
router.register('reservations', views.viewsets_reservation)

urlpatterns = [
    path('admin/', admin.site.urls),

    #1
    path('djangoStaticApi/', views.no_rest_no_model),

    #2
    path('djangoApiFromModel/', views.no_rest_with_model),

    #3
    #3.1 GET POST from rest framework function based view @api_view
    path('restAPI/FBV_list_customers/', views.Fbv_list),

    # 3.2 GET PUT DELETE from rest framework function based view @api_view
    path('restAPI/FBV_pk/<int:pk>', views.Fbv_Put_Delete),

    # 4
    # 4.1 GET POST from rest framework class based views(CBV) APIView
    path('restAPI/CBV_list_customers/', views.Cbv_list.as_view()),

    # 4.2 GET PUT DELETE from rest framework class based views(CBV) pk APIView
    path('restAPI/CBV_list_pk/<int:pk>', views.Cbv_list_pk.as_view()),

    #5
    # 5.1 GET POST from rest framework class based views(CBV) mixins
    path('restAPI/mixins_list_customers/', views.mixins_list.as_view()),

    # 5.2 GET PUT DELETE from rest framework class based views(CBV) pk mixins
    path('restAPI/mixins_list_customers/<int:pk>', views.mixins_pk.as_view()),

    # 6
    # 6.1 GET POST from rest framework class based views(CBV) generics
    path('restAPI/generics_list_customers/', views.generics_list.as_view()),

    # 6.2 GET PUT DELETE from rest framework class based views(CBV) pk mixins
    path('restAPI/generics_list_customers/<int:pk>', views.generics_pk.as_view()),

    #7 viewsets
    path('restAPI/viewsets/', include(router.urls)),

    # 8 find movie
    path('fbv/findmovie/', views.find_movie),
]

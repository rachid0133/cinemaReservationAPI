from django.contrib import admin
from django.urls import path
from ticketsApp import views

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
    path('restAPI/CBV_list_pk/<int:pk>', views.Cbv_list_pk.as_view())
]

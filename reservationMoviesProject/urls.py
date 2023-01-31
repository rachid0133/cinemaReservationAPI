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
    path('restAPI/FBV_pk/<int:pk>', views.Fbv_Put_Delete)
]

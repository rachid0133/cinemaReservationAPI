from django.contrib import admin
from django.urls import path
from ticketsApp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #1
    path('djangoStaticApi/', views.no_rest_no_model),

    #2
    path('djangoApiFromModel/', views.no_rest_with_model)
]

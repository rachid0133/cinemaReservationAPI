from django.contrib import admin
from django.urls import path
from ticketsApp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #1
    path('djangoStaticApi/', views.no_rest_no_model)
]

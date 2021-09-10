from django.urls import path,re_path
from .views import *

urlpatterns = [
    path('home/',home),
    path('hotel1',hotel1)
    ]

from django.urls import path
from django.urls.resolvers import URLPattern
from .views import index
URLPattern = [
    path('',index,name="index")
]

from django.urls import path
from .views import index,reparto,nosotros,login,registro,lista,productos,test



urlpatterns =[
    path('',index,name="index"),
    path('productos',productos,name="productos"),
    path('reparto',reparto,name="reparto"),
    path('nosotros',nosotros,name="nosotros"),
    path('login',login,name="login"),
    path('lista',lista,name="lista"),
    path('registro',registro,name="registro"),
    path('test',test,name="test"),
]
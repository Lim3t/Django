from django.urls import path
from .views import index,form_del_Cliente,form_Cliente,form_mod_Cliente,productos,reparto,nosotros,login,lista,registro,test,Cliente
from django.conf import settings


urlpatterns =[
    path('',index,name="index"),
    path('test',test,name="test"),
    path('productos',productos,name="productos"),
    path('reparto',reparto,name="reparto"),
    path('nosotros',nosotros,name="nosotros"),
    path('login',login,name="login"),
    path('lista',lista,name="lista"),
    path('registro',registro,name="registro"),
    path('form_Cliente',form_Cliente,name="form_Cliente"),
    path('form_mod_Cliente/<id>',form_mod_Cliente,name="form_mod_Cliente"),
    path('form_del_Cliente/<id>',form_del_Cliente,name="form_del_Cliente"),
    
]
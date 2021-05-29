from django.shortcuts import render

# Create your views here.
class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        super().__init__()


def index(request):
    return render(request,'core/index.html')

def reparto(request):
    return render(request,'core/reparto.html')

def nosotros(request):
    return render(request,'core/nosotros.html')

def login(request):
    return render(request,'core/login.html')

def registro(request):
    return render(request,'core/registro.html')

def lista(request):
    return render(request,'core/lista.html')

def productos(request):
    return render(request,'core/productos.html')

def test(request):

    persona=Persona("Elias",18)
    lista=["dato1","dato2","dato3"]
    context ={"nombre":"elias villar","persona":persona,"datos":lista}

    return render(request,'core/test.html',context)
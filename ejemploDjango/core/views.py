from django.shortcuts import render

# Create your views here.
class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        super().__init__()


def index(request):
    return render(request,'core/index.html')

def test(request):

    persona=Persona("alexander",18)
    lista=["dato1","dato2","dato3"]
    context ={"nombre":"elias villar","persona":persona,"datos":lista}

    return render(request,'core/index.html',context)
from ejemploDjango.ejemploDjango.settings import DATABASES
from django.shortcuts import render,redirect
from .models import Cliente
from .form import ClienteForm

# Create your views here.
def index(request):
    return render(request,'core/index.html')
    
class persona:
     def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        super().__init__()
        
        
def Test(request):
    
    clientes= Cliente.objects.all()
    
    datos={
        'clientes':clientes
    }
    return render(request,'core/test.html',datos)

def form_Cliente(request,id):
    if request.method =='POST':
        formulario = ClienteForm(request.POST)
        
        if formulario.is_valid:
            formulario.save()
            DATABASES['mensaje']='Guardado Correctamente'
            return render(request,'core/form_Cliente.html',data)


def form_mod_Cliente(request,id):
    cliente= Cliente.objects.get(nombre=id)
    data= {
        'form' :ClienteForm(instance=Cliente)
    }

    if request.method =='POST':
        formulario=ClienteForm(data=request.POST,instance=Cliente)
        
        if formulario.is_valid:
            formulario.save()
            data['mensaje']="guardado"
            return render(request,'core/form_Cliente.html',data)
        
def form_del_cliente(request,id):
    cliente= Cliente.objects.get(nombre=id)
    cliente.delete()
    return redirect(to="test")
    
    


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
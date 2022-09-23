from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from AppTurismo.forms import *
from AppTurismo.models import *
import random

@login_required
def inicio(request):
    return render(request, 'index.html')

@login_required
def paquete_turistico (request):
    
    if request.method == 'POST':
        mi_formulario = PaqueteTuristicoFormulario(request.POST)
        
        if mi_formulario.is_valid():
            
            data = mi_formulario.cleaned_data
            
            paquete1 = PaqueteTuristico(lugares=data.get('lugares'), fecha_de_entrada=data.get('fecha_de_entrada'),  fecha_de_salida=data.get('fecha_de_salida'))
            paquete1.save()
            
            return redirect('AppCliente')

        else:    
            messages.error(request, 'error del paquete')
        
            return redirect('AppTurismoPaquete')
        
    
    context = {
        'form': PaqueteTuristicoFormulario(),
        'method': 'POST',
        'title': 'PAQUETE TURISTICO',
        'Button_value': 'Enviar',
        
    }
    return render(request,'AppTurismo/formulario_universal.html', context)

@login_required
def cliente (request):
    names = ['Messi', 'Cr7', 'Alberto', 'Mirta', 'Raul', 'Ibai']
    choice_name = random.choice(names)
    
    if request.method == 'POST':
        formulario_cliente = ClienteFormulario(request.POST)
        
        if formulario_cliente.is_valid():
            data = formulario_cliente.cleaned_data
            
            cliente1 = Cliente(nombre= data.get('nombre'), apellido= data.get('apellido'),
                    email= data.get('email'), celular= data.get('celular'),
                    dni= data.get('dni'), empleado_asignado= choice_name, 
                    )
            try:
                cliente1.save()
                messages.info(request, 'Se guardo su paquete de viaje')
                return redirect('AppInicio')
            except:
                messages.error(request, 'error del cliente')
                return redirect('AppCliente')
    
    
    context = {
        'form': ClienteFormulario(),
        'method': 'POST',
        'title': 'FORMULARIO CLIENTE',
        'Button_value': 'Enviar',
        
    }
    
    return render(request, 'AppTurismo/formulario_universal.html', context)

@login_required
def busqueda_peticion_post (request):
    
    dni = request.GET.get('dni')
    cliente1 = Cliente.objects.filter(dni__exact=dni)
    idcliente = (cliente1)
    for id in idcliente:
        paquete_editar = PaqueteTuristico.objects.filter(id__exact=id.id)
    
    context = {
    'id': paquete_editar,
    'dni': cliente1,
    'title': 'BUSQUEDA CLIENTE',    
    }    
    return render(request, 'AppTurismo/busqueda_peticion_post.html', context)

@login_required
def busqueda_de_peticion(request):

    context = {
        'form': BusquedaPeticionFormulario(),
        'title': 'BUSQUEDA PETICIÓN',
        'Button_value': 'Buscar',
        
    }        
    
    return render(request, 'AppTurismo/busqueda_paquete.html', context)

@login_required
def elminar_peticion(request, dni):
    
    cliente_eliminar = Cliente.objects.get(dni=dni)
    cliente_eliminar.delete()
    messages.info(request, f'El Cliente {cliente_eliminar} fue eliminado')
    
    return redirect('AppInicio')

@login_required
def editar_cliente(request, dni):
        try:
            cliente_editar = Cliente.objects.get(dni=dni)
            id = cliente_editar.id
            paquete_editar = PaqueteTuristico(id=id)
            
            
            if request.method == 'POST':
                mi_formulario = ClienteFormulario(request.POST)
                mi_formulario1 = PaqueteTuristicoFormulario(request.POST)
                
                if mi_formulario.is_valid() and mi_formulario1.is_valid():
                    data = mi_formulario.cleaned_data
                    data1 = mi_formulario1.cleaned_data
                    
                    cliente_editar.nombre = data.get('nombre')
                    cliente_editar.apellido = data.get('apellido')
                    cliente_editar.email = data.get('email')
                    cliente_editar.celular = data.get('celular')
                    cliente_editar.dni = data.get('dni')
                    cliente_editar.save()
                    
                    paquete_editar.lugares = data1.get('lugares')
                    paquete_editar.fecha_de_entrada = data1.get('fecha_de_entrada')
                    paquete_editar.fecha_de_salida = data1.get('fecha_de_salida')
                    paquete_editar.save()
                    
                    messages.info(request,'Se actualizo!')
                    return redirect('AppInicio')
            
                    
        except:    
            messages.info(request,'error, no se actualizo')
        
        
        context = {
            'title': 'EDITAR CLIENTE',
            'method': 'POST',
            'Button_value': 'Editar',
            'info': 'Modificar Paquete de viaje contratado:',
            'form': ClienteFormulario(
                initial= {
                    'dni': cliente_editar.dni,
                    'nombre': cliente_editar.nombre,
                    'apellido': cliente_editar.apellido,
                    'email': cliente_editar.email,
                    'celular': cliente_editar.celular,   
                }
            ),
            'form1': PaqueteTuristicoFormulario(
                initial={
                    'lugares': paquete_editar.lugares,
                    'fecha_de_entrada': paquete_editar.fecha_de_entrada,
                    'fecha_de_salida': paquete_editar.fecha_de_salida
                    
                }
            )
        }
    
        return render(request, 'AppTurismo/formulario_universal.html', context)
    

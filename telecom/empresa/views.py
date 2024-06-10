from django.shortcuts import render
from itertools import chain

from django.db.models import OuterRef, Subquery


# Create your views here.
from django.shortcuts import render, redirect
from .forms import ClienteForm
# views.py
from .forms import ClienteForm
from django.shortcuts import render
from .models import Cliente, Contacto, Direccion, Compra, Servicio, Subservicio, Trabajador, Componente, RealizarCompra, CompraSubservicio, ServicioSubservicio, SubservicioComponente, PagoSalario

def index(request):
    return render(request, 'empresas/layout.html')



def principal(request):
    return render(request, 'empresas/principal.html')

def view_all_data(request):
    clientes = Cliente.objects.all()
    contactos = Contacto.objects.all()
    direcciones = Direccion.objects.all()
    compras = Compra.objects.all()
    servicios = Servicio.objects.all()
    subservicios = Subservicio.objects.all()
    trabajadores = Trabajador.objects.all()
    componentes = Componente.objects.all()
    realizar_compras = RealizarCompra.objects.all()
    compra_subservicios = CompraSubservicio.objects.all()
    servicio_subservicios = ServicioSubservicio.objects.all()
    subservicio_componentes = SubservicioComponente.objects.all()
    pagos_salarios = PagoSalario.objects.all()

    return render(request, 'empresas/all_data_table.html', {
        'clientes': clientes,
        'contactos': contactos,
        'direcciones': direcciones,
        'compras': compras,
        'servicios': servicios,
        'subservicios': subservicios,
        'trabajadores': trabajadores,
        'componentes': componentes,
        'realizar_compras': realizar_compras,
        'compra_subservicios': compra_subservicios,
        'servicio_subservicios': servicio_subservicios,
        'subservicio_componentes': subservicio_componentes,
        'pagos_salarios': pagos_salarios,
    })


#este es formulario para las views para crud
def clienteFormView(request):
    form = ClienteForm()
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, 'empresas/orders.html', context)


def showView(request):
    clientes = Cliente.objects.all()
    context = {'clientes': clientes}
    return render(request, 'empresas/show.html', context)


def updateView(request, f_nit):
    clientes = Cliente.objects.get(nit=f_nit)
    form = ClienteForm(instance=clientes)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=clientes)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, 'empresas/orders.html', context)

def deleteView(request, f_nit):
    obj = Cliente.objects.get(nit=f_nit)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    context = {'obj': obj}
    return render(request, 'empresas/confirmation.html', context)


def join_example(request):
    clientes = Cliente.objects.all()
    contactos = Contacto.objects.all()
    direcciones = Direccion.objects.all()
    compras = Compra.objects.all()
    servicios = Servicio.objects.all()
    subservicios = Subservicio.objects.all()
    trabajadores = Trabajador.objects.all()
    componentes = Componente.objects.all()
    realizar_compras = RealizarCompra.objects.all()
    compra_subservicios = CompraSubservicio.objects.all()
    servicio_subservicios = ServicioSubservicio.objects.all()
    subservicio_componentes = SubservicioComponente.objects.all()
    pagos_salarios = PagoSalario.objects.all()

    return render(request, 'empresas/joins.html', {
        'clientes': clientes,
        'contactos': contactos,
        'direcciones': direcciones,
        'compras': compras,
        'servicios': servicios,
        'subservicios': subservicios,
        'trabajadores': trabajadores,
        'componentes': componentes,
        'realizar_compras': realizar_compras,
        'compra_subservicios': compra_subservicios,
        'servicio_subservicios': servicio_subservicios,
        'subservicio_componentes': subservicio_componentes,
        'pagos_salarios': pagos_salarios,
    })



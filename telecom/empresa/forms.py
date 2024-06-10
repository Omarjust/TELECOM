from django import forms
from .models import Cliente, Contacto, Direccion, Compra, Servicio, Subservicio, Trabajador, Componente, RealizarCompra, CompraSubservicio, ServicioSubservicio, SubservicioComponente, PagoSalario

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

        labels = {
            'nit' : 'Nit cliente',
            'nombre_cliente': 'nombre cliente'
        }

        widgets ={
            'nit':forms.NumberInput(attrs={'placeholder': 'eg. 101'}),
            'nombre_cliente': forms.TextInput(attrs={'placeholder': 'eg. Omarjust'})
        }
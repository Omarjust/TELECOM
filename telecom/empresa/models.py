
# models.py
from django.db import models


class Cliente(models.Model):
    nit = models.CharField(primary_key=True, max_length=20)
    nombre_cliente = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_cliente

class Contacto(models.Model):
    nit = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"Contacto de {self.telefono}"

class Direccion(models.Model):
    nit = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return f"Dirección de {self.nit.nombre_cliente}"

class Compra(models.Model):
    id_compra = models.AutoField(primary_key=True)
    fecha_compra = models.DateField()
    nit_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"compra numero: {self.id_compra} {self.nit_cliente.nombre_cliente}"

class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    nombre_servicio = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_servicio

class Subservicio(models.Model):
    id_subservicio = models.AutoField(primary_key=True)
    nombre_subservicio = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"subservicio: {self.nombre_subservicio}"

class Trabajador(models.Model):
    id_trabajador = models.AutoField(primary_key=True)
    nombre_trabajador = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_trabajador

class Componente(models.Model):
    id_componente = models.AutoField(primary_key=True)
    nombre_componente = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_componente

class RealizarCompra(models.Model):
    nit_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_compra = models.ForeignKey(Compra, on_delete=models.CASCADE)

    def __str__(self):
        return f"compra de {self.nit_cliente} numero: {self.id_compra}"


class CompraSubservicio(models.Model):
    id_compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    id_subservicio = models.ForeignKey(Subservicio, on_delete=models.CASCADE)

    def __str__(self):
        return f"compra de {self.id_subservicio} numero: {self.id_compra}"

class ServicioSubservicio(models.Model):
    id_servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    id_subservicio = models.ForeignKey(Subservicio, on_delete=models.CASCADE)

    def __str__(self):
        return f"servicio {self.id_servicio} numero: {self.id_subservicio}"

class SubservicioComponente(models.Model):
    id_subservicio = models.OneToOneField(Subservicio, primary_key=True, on_delete=models.CASCADE)
    id_componente = models.ForeignKey(Componente, on_delete=models.CASCADE)
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"compra de {self.id_componente.nombre_componente} numero: {self.id_subservicio} al precio: {self.precio_compra}"

class PagoSalario(models.Model):
    id_pago = models.AutoField(primary_key=True)
    id_trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    fecha_pago = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"pago de {self.id_trabajador.nombre_trabajador} numero: {self.id_pago}"


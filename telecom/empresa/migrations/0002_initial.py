# Generated by Django 5.0.3 on 2024-03-21 00:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('nit', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombre_cliente', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Componente',
            fields=[
                ('id_componente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_componente', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id_servicio', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_servicio', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subservicio',
            fields=[
                ('id_subservicio', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_subservicio', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('precio_venta', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id_trabajador', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_trabajador', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id_compra', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_compra', models.DateField()),
                ('nit_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(max_length=20)),
                ('nit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=200)),
                ('nit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='RealizarCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.compra')),
                ('nit_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='ServicioSubservicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.servicio')),
                ('id_subservicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.subservicio')),
            ],
        ),
        migrations.CreateModel(
            name='CompraSubservicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.compra')),
                ('id_subservicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.subservicio')),
            ],
        ),
        migrations.CreateModel(
            name='PagoSalario',
            fields=[
                ('id_pago', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_pago', models.DateField()),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id_trabajador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.trabajador')),
            ],
        ),
        migrations.CreateModel(
            name='SubservicioComponente',
            fields=[
                ('id_subservicio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='empresa.subservicio')),
                ('precio_compra', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id_componente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.componente')),
            ],
        ),
    ]

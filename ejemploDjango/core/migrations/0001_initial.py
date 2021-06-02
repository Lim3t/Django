# Generated by Django 3.2.3 on 2021-06-02 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='id de categoria')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='nombre de la categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=6, verbose_name='Nombre Cliente')),
                ('apellido', models.CharField(max_length=20, verbose_name='Apellido Cliente')),
                ('direccion', models.CharField(blank=True, max_length=20, null=True, verbose_name='Direccion Cliente')),
                ('correo', models.CharField(blank=True, max_length=20, null=True, verbose_name='Correo Cliente')),
                ('comuna', models.CharField(blank=True, max_length=20, null=True, verbose_name='Comuna Cliente')),
                ('edad', models.CharField(blank=True, max_length=20, null=True, verbose_name='Edad Cliente')),
                ('comentario', models.CharField(blank=True, max_length=200, null=True, verbose_name='Comentario Cliente')),
                ('Categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
    ]

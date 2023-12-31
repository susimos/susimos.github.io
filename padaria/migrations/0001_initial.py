# Generated by Django 4.2.7 on 2023-11-26 13:37

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('sobrenome', models.CharField(max_length=50)),
                ('cpf', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=50)),
            ],
            managers=[
                ('objetos', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=255)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
            managers=[
                ('objetos', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='padaria.cliente')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='padaria.produto')),
            ],
            managers=[
                ('objetos', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Fila',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='padaria.venda')),
            ],
            managers=[
                ('objetos', django.db.models.manager.Manager()),
            ],
        ),
    ]

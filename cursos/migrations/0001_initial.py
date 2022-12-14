# Generated by Django 3.2 on 2022-11-24 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='criacao')),
                ('atualizado', models.DateField(auto_now=True, verbose_name='atualizacao')),
                ('ativo', models.BooleanField(default=True, verbose_name='ativo')),
                ('titulo', models.CharField(max_length=255, verbose_name='Nome')),
                ('url', models.URLField(unique=True)),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='criacao')),
                ('atualizado', models.DateField(auto_now=True, verbose_name='atualizacao')),
                ('ativo', models.BooleanField(default=True, verbose_name='ativo')),
                ('nome', models.CharField(max_length=255, verbose_name='nome')),
                ('email', models.EmailField(max_length=254)),
                ('comentario', models.TextField(blank=True, default='')),
                ('avaliacao', models.DecimalField(decimal_places=1, max_digits=2)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avaliacoes', to='cursos.curso')),
            ],
            options={
                'verbose_name': 'Avaliação',
                'verbose_name_plural': 'Avaliações',
                'unique_together': {('email', 'curso')},
            },
        ),
    ]

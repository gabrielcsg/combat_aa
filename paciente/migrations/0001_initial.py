# Generated by Django 2.2.6 on 2019-10-04 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('data_nascimento', models.DateField()),
                ('tipo_sanguineo', models.CharField(max_length=3)),
                ('sexo', models.CharField(max_length=1)),
                ('endereco', models.CharField(max_length=150)),
                ('patologia', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=20)),
            ],
        ),
    ]

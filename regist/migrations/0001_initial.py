# Generated by Django 2.0.7 on 2023-01-08 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Getnumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('Idnumber', models.CharField(max_length=15)),
                ('birthday', models.DateField()),
                ('sex', models.CharField(max_length=10)),
                ('reIdentity', models.CharField(max_length=200)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('Idnumber', models.CharField(max_length=15)),
                ('birthday', models.DateField()),
                ('sex', models.CharField(max_length=10)),
                ('Identity', models.CharField(max_length=200)),
                ('tel', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'register',
            },
        ),
    ]

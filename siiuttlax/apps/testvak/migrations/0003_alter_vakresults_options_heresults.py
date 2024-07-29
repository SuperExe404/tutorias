# Generated by Django 5.0.6 on 2024-07-18 20:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0003_admin'),
        ('testvak', '0002_remove_heinterview_b5_remove_heinterview_c1_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vakresults',
            options={'verbose_name': 'Resultado de VAK', 'verbose_name_plural': 'Resultados de VAK'},
        ),
        migrations.CreateModel(
            name='HEResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contadorHE', models.IntegerField(default=0)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='he_results', to='academy.student')),
            ],
            options={
                'verbose_name': 'Resultado de HE',
                'verbose_name_plural': 'Resultados de HE',
            },
        ),
    ]

# Generated by Django 3.1 on 2020-08-08 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial_models'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Barrios',
            new_name='Barrio',
        ),
        migrations.AlterModelOptions(
            name='barrio',
            options={'verbose_name': 'Barrio', 'verbose_name_plural': 'Barrios'},
        ),
        migrations.AlterModelOptions(
            name='liderrespbarrio',
            options={'verbose_name': 'liderRespBarrio', 'verbose_name_plural': 'liderRespBarrio'},
        ),
    ]

# Generated by Django 2.2.6 on 2020-10-29 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0002_auto_20201029_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='habilidades',
            field=models.ManyToManyField(to='personas.Habilidades'),
        ),
    ]

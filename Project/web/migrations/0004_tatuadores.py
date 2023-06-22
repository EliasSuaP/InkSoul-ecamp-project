# Generated by Django 4.2 on 2023-06-21 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_reserva'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tatuadores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('url', models.URLField()),
                ('descripcion', models.TextField()),
            ],
        ),
    ]
# Generated by Django 4.2.1 on 2023-05-17 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='room_number',
            field=models.PositiveIntegerField(default='0', verbose_name='Номер комнаты'),
        ),
    ]

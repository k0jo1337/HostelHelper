# Generated by Django 4.2.1 on 2023-05-17 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_customuser_room_number'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Requests',
            new_name='Appeal',
        ),
    ]

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    surname = models.CharField('Отчество', max_length=25, default='')
    room_number = models.PositiveIntegerField('Номер комнаты', default=0)




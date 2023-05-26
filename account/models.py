from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    surname = models.CharField('Отчество', max_length=25, default='')
    room_number = models.PositiveIntegerField('Номер комнаты', default='0')
    phone = models.CharField('Номер телефона', max_length=11, default='')
    university = models.CharField('Институт', max_length=50, default='')
    hostel = models.PositiveIntegerField('Номер общежития', default='0')

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    avatar = models.ImageField(
        default='avatar.jpg',
        upload_to='profile_images'
    )

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.avatar.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)


class Appeal(models.Model):
    subject = models.CharField(max_length=50, verbose_name='Тема')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    content = models.TextField(verbose_name='Содержание обращения')
    user = models.ForeignKey(CustomUser, verbose_name='Пользователь', on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(max_length=50, verbose_name='Е-майл')
    ip_address = models.GenericIPAddressField(verbose_name='IP отправителя', blank=True, null=True)

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'
        ordering = ['-time_create']

    def __str__(self):
        return f'Вам письмо от {self.email}'

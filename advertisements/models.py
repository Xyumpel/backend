from django.conf import settings
from django.db import models


class AdvertisementStatusChoices(models.TextChoices):
    OPEN = "OPEN", "Открыто"
    CLOSED = "CLOSED", "Закрыто"

class Advertisement(models.Model):
    title = models.TextField(verbose_name='Заголовок')
    description = models.TextField(default='', verbose_name='Описание')
    status = models.TextField(choices=AdvertisementStatusChoices.choices, default=AdvertisementStatusChoices.OPEN, verbose_name='Cтатус')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Создатель')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Cоздано')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='Обновленно')

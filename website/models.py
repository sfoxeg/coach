from django.db import models


class Services(models.Model):
    enable = models.BooleanField(default=False, verbose_name='Доступна')
    title = models.CharField(max_length=150, verbose_name='Название')
    desc = models.TextField(verbose_name='Описание услуги')
    image = models.FileField(verbose_name='Изображение')
    price = models.IntegerField(verbose_name='Цена')
    credit_type = models.IntegerField(verbose_name='Тип оплаты (0 - собственные средства, 2- кредит, 3 - рассрочка)')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услугу'
        verbose_name_plural = 'Услуги'

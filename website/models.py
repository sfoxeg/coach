from django.db import models


class Services(models.Model):
    enable = models.BooleanField(default=False, verbose_name='Доступна')
    title = models.CharField(max_length=150, verbose_name='Название')
    desc = models.TextField(verbose_name='Описание услуги')
    image = models.FileField(verbose_name='Изображение')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    CREDIT_TYPES = (
        (0, 'собственные средства'),
        (1, 'кредит'),
        (2, 'рассрочка')
    )
    credit_type = models.SmallIntegerField(choices=CREDIT_TYPES, default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услугу'
        verbose_name_plural = 'Услуги'


class Mastermind_reg(models.Model):
    fio = models.CharField(max_length=300, verbose_name='ФИО')
    phone = models.SmallIntegerField(verbose_name='Телефон')
    email = models.EmailField(verbose_name='Почта')
    request = models.TextField(verbose_name='Запрос')

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Зарегистрировались на мм'

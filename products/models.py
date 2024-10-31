from django.core.validators import MinValueValidator
from django.db import models
from djmoney.models.fields import MoneyField


class Type(models.Model):
    name = models.CharField('Название', max_length=15, unique=True)
    description = models.CharField('Описание',
                                   max_length=150,
                                   blank=True, null=True)

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField('Название', max_length=20, unique=True)
    price = MoneyField('Цена',
                       max_digits=6,
                       decimal_places=2,
                       default_currency='RUB')
    amount = models.PositiveIntegerField('Количество',
                                         validators=[MinValueValidator(1)])
    barcode = models.CharField('Штрихкод', max_length=15, unique=True)
    date_of_update = models.DateTimeField('Дата обновления', auto_now=True)
    type = models.ForeignKey(Type,
                             on_delete=models.CASCADE, verbose_name='Тип')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

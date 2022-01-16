from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name="имя", max_length=64, unique=True)
    description = models.TextField(
        verbose_name='описание',
        blank=True,
        null=True,
    )

    # Эти поля делать обязательно!
    created = models.DateTimeField(
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f'{self.name} - {self.id} -- {self.created}'

    # тут обязательно законченно!

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        verbose_name='категория',
    )

    name = models.CharField(
        verbose_name='имя продукта',
        max_length=128,
    )

    image = models.ImageField(
        upload_to='products_images',
        blank=True,
        verbose_name='картинка',
    )

    short_desk = models.CharField(
        verbose_name='краткое описание товара',
        max_length=60,
        blank=True,
    )

    description = models.TextField(
        verbose_name='описание товара',
        blank=True,
    )

    price = models.DecimalField(
        verbose_name='цена продукта',
        max_digits=8,
        decimal_places=2,
        default=0,
    )

    quantity = models.PositiveIntegerField(
        verbose_name='количество на складе',
        default=0,
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

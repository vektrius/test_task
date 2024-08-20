from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название категории')
    description = models.TextField(verbose_name='Описание')
    sort = models.IntegerField(verbose_name='Сортировка')
    active = models.BooleanField(verbose_name='Активна', default=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    COLORS = (
        ('red', 'Красный'),
        ('green', 'Зеленый'),
        ('blue', 'Синий'),
    )
    title = models.CharField(max_length=255, verbose_name='Название продукта')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория',
        related_name='products'
    )
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    color = models.CharField(max_length=255, verbose_name='Цвет', choices=COLORS)

    def __str__(self):
        return self.title


class Review(models.Model):
    body = models.TextField(verbose_name='Текст отзыва')
    rate = models.IntegerField(verbose_name='Оценка')
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Продукт',
        related_name='reviews'
    )
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Пользователь',
        related_name='reviews'
    )
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.product.title} - {self.rate}'

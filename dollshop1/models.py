from django.contrib.auth.models import User
from django.db import models



class Category(models.Model):

    name = models.CharField(max_length=255, unique=True, verbose_name='Название')

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    STATUS = (('В наличии', 'В наличии'), ('Нет в наличии', 'Нет в наличии'))

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, verbose_name='Категория')
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(max_length=1300, verbose_name='Описание')
    image = models.ImageField(default='no_image.png', upload_to='product_image/', blank=True, null=True,
                              verbose_name='Изображение')
    price = models.DecimalField(decimal_places=0, max_digits=9, default=0, verbose_name='Цена')
    date_create = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, choices=STATUS, default=STATUS[1], verbose_name='Статус')

    def __str__(self):
        return f'{self.name}, {self.category}, {self.price}, {self.date_create}'


class Commentary(models.Model):

    user = models.ForeignKey(User, default=User, on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    text = models.TextField(max_length=2000, verbose_name='Комментарий')
    date_create = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.user}, {self.product}, {self.date_create}'


class Wishlist(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')

    def __str__(self):
        return f'{self.user}, {self.product}'


class Cart(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveIntegerField(default=1)
    price_and_quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.user}, {self.product}'


    def get_quantity_sum(self):
        self.price_and_quantity += self.product.price * self.quantity
        return self.price_and_quantity
from django.contrib.auth.models import User
from django.db import models


CATEGORY = (
    ('транспорт', 'транспорт'),
    ('недвижимость', 'недвижимость'),
    ('электроника', 'электроника'),
    ('услуги', 'услуги'),
    ('работа', 'работа'),
    ('животные', 'животные'),
    ('личные вещи', 'личные вещи')

)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name


class Product(models.Model):

    title = models.CharField(max_length=255, blank=True, default='', verbose_name='Наименования')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(verbose_name='Описания товара')
    slug = models.SlugField(unique=True)
    category = models.CharField(choices=CATEGORY, default=' ', max_length=255)
    created_by = models.ForeignKey(User, related_name='product', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.category}: {self.title}'









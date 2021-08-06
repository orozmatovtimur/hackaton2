from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    slug = models.SlugField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        if self.parent:
            return f"{self.parent} -> {self.name}"
        return self.name


class Product(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=10,
                              decimal_places=3)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

# class Reviews(models.Model):
#     """Отзыв"""
#     email = models.EmailField()
#     name = models.CharField(max_length=100)
#     text = models.CharField(max_length=3000)
#     dish = models.ForeignKey(Dish, verbose_name='Блюдо ', on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"{self.name} - {self.dish}"
#
#     class Meta:
#         verbose_name = "Отзыв"
#         verbose_name_plural = "Отзывы"

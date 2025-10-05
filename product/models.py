from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.FloatField()

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField(blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True)
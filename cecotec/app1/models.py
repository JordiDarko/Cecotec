from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=CASCADE)
    quantity = models.IntegerField()
    

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    shipping_charges = models.FloatField(null=True)
    observations = models.TextField()
    ordered = models.BooleanField(default=False)

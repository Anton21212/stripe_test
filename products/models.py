from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.aggregates import Sum


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name

    @property
    def get_price(self):
        return f"{self.price / 100:.2f}"


class Order(models.Model):
    items = models.ManyToManyField(Item)

    @property
    def total_cost(self):
        total = Item.objects.all().aggregate(Sum('price'))
        total = total.get("price__sum")
        return total

    @property
    def total_cost_for_html(self):
        total = Item.objects.all().aggregate(Sum('price'))
        total = total.get("price__sum")
        return f"{total / 100:.2f}"

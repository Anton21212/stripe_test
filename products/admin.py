from django.contrib import admin

from products.models import Item, Order

admin.site.register(Item)
admin.site.register(Order)


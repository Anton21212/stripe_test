from django.views.generic import TemplateView
from config import settings
from .models import Item, Order


class ItemInfoView(TemplateView):
    template_name = 'item_info.html'

    def get_context_data(self, **kwargs):
        try:
            item = Item.objects.get(id=kwargs['id'], )
        except:
            raise ValueError("C таким id нету товара")
        else:
            context = super().get_context_data(**kwargs)
            context.update({
                "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY,
                "item": item,
            })
            return context


class ItemsInfoView(TemplateView):
    template_name = 'items_info.html'

    def get_context_data(self, **kwargs):
        try:
            orders = Order.objects.all()
        except:
            raise ValueError
        else:
            context = super().get_context_data(**kwargs)
            context.update({
                "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY,
                "orders": orders,
            })

        return context

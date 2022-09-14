from django.views import View
import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views.generic import TemplateView

from products.models import Item, Order

stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"


class CreateCheckoutSessionViews(View):

    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()
        YOUR_DOMAIN = 'http://127.0.0.1:8000'
        total_cost = ''
        names_list = []
        for order in orders:
            total_cost = order.total_cost
            for item in order.items.all():
                names_list.append(item.name)
        names_str = ",".join(names_list)
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'currency': 'USD',
                        'unit_amount': total_cost,
                        'product_data': {
                            'name': names_str,
                        }
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success',
            cancel_url=YOUR_DOMAIN + '/cancel')
        return JsonResponse({
            'id': checkout_session.id
        })


class CreateCheckoutSessionView(View):
    def get(self, request, *args, **kwargs):
        item_id = self.kwargs["id"]
        item = Item.objects.get(id=item_id)
        YOUR_DOMAIN = 'http://127.0.0.1:8000'
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'currency': 'USD',
                        'unit_amount': item.price,
                        'product_data': {
                            'name': item.name,
                        }
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success',
            cancel_url=YOUR_DOMAIN + '/cancel')
        return JsonResponse({
            'id': checkout_session.id
        })

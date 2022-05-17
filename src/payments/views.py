from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from .settings import STRIPE_SECRET_KEY, STRIPE_PUBLISHABLE_KEY
from .models import Item
import stripe
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def CreateCheckoutSession(request, pk):
    product = get_object_or_404(Item, pk=pk)
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'product_data': {
                                'name': product.name,
                            },
                            'unit_amount': int(product.price * 100),
                        },
                        'quantity': 1,
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


class ItemDetailView(DetailView):
    model = Item
    template_name = "item_detail.html"
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        context.update({
            "STRIPE_PUBLISHABLE_KEY": STRIPE_PUBLISHABLE_KEY
        })
        return context

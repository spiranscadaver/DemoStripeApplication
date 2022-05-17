from django.contrib import admin
from django.urls import path
from payments.views import CreateCheckoutSession, ItemDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buy/<int:pk>', CreateCheckoutSession, name='create_checkout_session'),
    path('item/<int:pk>', ItemDetailView.as_view(), name='detail'),
]

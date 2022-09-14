"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from products.views import ItemInfoView, ItemsInfoView
from stripe_api.views import CreateCheckoutSessionView, CancelView, SuccessView,CreateCheckoutSessionViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cancel/', CancelView.as_view(), name='cansel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('buy/<id>/', CreateCheckoutSessionView.as_view(), name='buy'),
    path('item/<id>/', ItemInfoView.as_view(), name='item_info'),
    path('item_all/', ItemsInfoView.as_view(), name='item_info_all'),
    path('buy_all/', CreateCheckoutSessionViews.as_view(), name='buy_all'),
]

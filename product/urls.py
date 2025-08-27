from django.urls import path
from product import views

urlpatterns = [
    path("shop/", views.shop, name="shop"),
]

from django.shortcuts import render
from product.models import Product
def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})

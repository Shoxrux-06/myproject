from django.shortcuts import render

def shop(request):
    products = [
        {"name": "RTX 5050", "price": 300, "image": "products/rtx.png"},
        {"name": "RTX 6060", "price": 200000, "image": "products/rtxx.png"},
    ]
    return render(request, 'product/shop.html', {'products': products})

from django.shortcuts import render
from product.models import Product
def product(request):
    pass

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {'products': products})


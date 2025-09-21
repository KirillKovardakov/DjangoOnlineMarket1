from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Product


# Create your views here.
def home(request):
    last_three_products = Product.objects.order_by('-id')[:3]
    products = Product.objects.all()
    print(last_three_products)
    context = {'products': products}
    return render(request, 'home.html',context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        return HttpResponse(f'Сбасибо, {name}! Сообщение получено.')
    return render(request, 'contacts.html')


def product(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product':product}
    return render(request,'product.html',context)
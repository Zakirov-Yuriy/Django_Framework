from django.shortcuts import render
from mainapp.models import Product

def index(request):
    title = 'geekshop'
    products = Product.objects.all()[:4]

    context = {
        'title': title,
        'products': products,
    }
    return render(request, 'index.html', context=context)


def contacts(request):
    return render(request, 'contact.html')

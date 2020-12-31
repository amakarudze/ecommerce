from django.core.paginator import Paginator
from django.shortcuts import render

from . models import Order, Product

# Create your views here.


def index(request):
    products = Product.objects.all()
    item_name = request.GET.get('item_name')
    # Search code
    if item_name != '' and item_name is not None:
        products = products.filter(title__icontains=item_name)

    # Paginator code
    paginator = Paginator(products, 4)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, 'shop/index.html', {'products': products})


def detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'shop/detail.html', {'product': product})


def checkout(request):
    if request.method == 'POST':
        items = request.POST['items']
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        address2 = request.POST['address2']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']

        order = Order(items=items, name=name, email=email, address=address, address2=address2, city=city,
                      state=state, zipcode=zipcode)
        order.save()

    return render(request, 'shop/checkout.html')

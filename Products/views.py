from django.shortcuts import render
from Products.models import Product, Hashtag


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        contex = {
            'products': [
                {
                    'id': product.id,
                    'title': product.title,
                    'image': product.image,
                    'quantity': product.quantity,
                    'price': product.price,
                    'hashtags': product.hashtags.all()
                } for product in products
            ]
        }

        return render(request, 'products/products.html', context=contex)


def hashtags_view(request):
    if request.method == 'GET':
        hashtags = Hashtag.objects.all()

        context = {
            'hashtags': hashtags
        }

        return render(request, 'products/hashtags.html', context=context)


def product_detail_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)

        context = {
            'product': product,
            'reviews': product.review_set.all
        }

        return render(request, 'products/detail.html', context=context)

from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    extra_context = {'title': 'Всячина', 'description_title': 'Всячина - это онлайн магазин абсолютно разных товаров '
                                                              '(от хлеба до крыла от самолёта) по доступной цене и '
                                                              'отличного качества'}


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'
    extra_context = {'title': 'Товары', 'description_title': 'Самые лучшие товары отличного качества'}


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print(f"Имя:{name}\nТелефон: {phone}\nСообщение: {message}")

    context = {'title': 'Контакты', 'description_title': 'Свяжитесь с нами и мы вам обязательно поможем!'}
    return render(request, 'catalog/contacts.html', context)

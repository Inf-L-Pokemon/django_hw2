from django.shortcuts import render

from catalog.models import Product


def home(request):
    context = {'object_list': Product.objects.all(),
               'title': 'Всячина',
               'description_title': 'Всячина - это онлайн магазин абсолютно разных товаров'
                                    '(от хлеба до крыла от самолёта) по доступной цене и отличного качества'}
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print(f"Имя:{name}\nТелефон: {phone}\nСообщение: {message}")

    context = {'title': 'Контакты', 'description_title': 'Свяжитесь с нами и мы вам обязательно поможем!'}
    return render(request, 'catalog/contacts.html', context)


def product(request, pk):
    context = {'object': Product.objects.get(pk=pk),
               'title': 'Товары', 'description_title': 'Самые лучшие товары отличного качества'}
    return render(request, 'catalog/product.html', context)

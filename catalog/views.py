from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


class ProductListView(ListView):
    model = Product
    extra_context = {'title': 'Всячина', 'description_title': 'Всячина - это онлайн магазин абсолютно разных товаров '
                                                              '(от хлеба до крыла от самолёта) по доступной цене и '
                                                              'отличного качества'}


class ProductDetailView(DetailView):
    model = Product
    extra_context = {'title': 'Товары', 'description_title': 'Самые лучшие товары отличного качества'}


class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'
    extra_context = {'title': 'Контакты', 'description_title': 'Свяжитесь с нами и мы вам обязательно поможем!'}

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print(f"Имя:{name}\nТелефон: {phone}\nСообщение: {message}")
        return HttpResponseRedirect('/')

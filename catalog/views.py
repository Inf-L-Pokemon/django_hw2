from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.urls.base import reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


class ProductListView(ListView):
    model = Product
    extra_context = {'title': 'Всячина', 'description_title': 'Всячина - это онлайн магазин абсолютно разных товаров '
                                                              '(от хлеба до крыла от самолёта) по доступной цене и '
                                                              'отличного качества'}

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        product_list = Product.objects.all()

        for product in product_list:
            versions = Version.objects.filter(product=product)
            if versions.count() == 0:
                continue
            current_version = versions.filter(is_current=True)
            if current_version:
                product.name_version = current_version.last().name
                product.number_version = current_version.last().number
        context_data['object_list'] = product_list
        return context_data


class ProductDetailView(DetailView):
    model = Product
    extra_context = {'title': 'Товары', 'description_title': 'Самые лучшие товары отличного качества'}


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'
    extra_context = {'title': 'Контакты', 'description_title': 'Свяжитесь с нами и мы вам обязательно поможем!'}

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print(f"Имя:{name}\nТелефон: {phone}\nСообщение: {message}")
        return HttpResponseRedirect('/')

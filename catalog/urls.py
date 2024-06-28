from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactsTemplateView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView, CategoryListView, PlugTemplateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('product/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('plug/', PlugTemplateView.as_view(), name='plug')
]

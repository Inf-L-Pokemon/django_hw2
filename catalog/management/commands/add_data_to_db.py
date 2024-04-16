from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category_for_create = []
        product_for_create = []

        category_list = [
            {"name": "Смартфоны", "description": "Крутые телефоны без кнопок и с большим экраном", "pk": 1},
            {"name": "Фрукты", "description": "", "pk": 2},
            {"name": "Напитки", "description": "Различные безалкогольные напитки, соки, воды", "pk": 3}
        ]

        for category in category_list:
            category_for_create.append(Category(**category))

        Category.objects.bulk_create(category_for_create)

        product_list = [
            {"name": "IPhone 38", "description": "Самый крутой телефон с 15 камерами формата 7D",
             "category": Category.objects.get(pk=1), "price": 4000000.98},
            {"name": "Яблоко", "description": "Сладчайший фрукт из солнечной Гренландии",
             "category": Category.objects.get(pk=2), "price": 15.00},
            {"name": "Кола", "description": "Старый русский древний напиток",
             "category": Category.objects.get(pk=3), "price": 85.26},
            {"name": "Яга", "description": "Лучшее зелье от Бабы-Яги",
             "category": Category.objects.get(pk=3), "price": 102.33},
            {"name": "Арбуз", "description": "Арбуз - это не фрукт и не ягода, арбуз - это тыквина",
             "category": Category.objects.get(pk=2), "price": 14.88}
        ]

        for product in product_list:
            product_for_create.append(Product(**product))

        Product.objects.bulk_create(product_for_create)

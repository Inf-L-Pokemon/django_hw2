from django.core.cache import cache

from catalog.models import Category
from config.settings import CACHE_ENABLED


def get_category_list():
    if not CACHE_ENABLED:
        return Category.objects.all()

    key = "category_list"
    objects = cache.get(key)
    if objects is not None:
        return objects

    objects = Category.objects.all()
    cache.set(key, objects)
    return objects

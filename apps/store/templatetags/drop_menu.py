from django import template

from apps.store.models import Category

register = template.Library()

@register.inclusion_tag("core/drop_menu.html")
def drop_menu():
    categories = Category.objects.all()
    return{ 'categories': categories}
from django.shortcuts import render, get_object_or_404
from menu.models import Menu


def index(request):
    parent_menus = Menu.objects.filter(parent=None)
    context = {
        'parent_menus': parent_menus,
        'current_menu': None,
    }
    return render(request, 'index.html', context)


def categories(request, parent_slug, child_slug=None):
    parent_menus = Menu.objects.filter(parent=None)

    if child_slug:
        current_menu = get_object_or_404(Menu, slug=child_slug, parent__slug=parent_slug)
    else:
        current_menu = get_object_or_404(Menu, slug=parent_slug)

    context = {
        'parent_menus': parent_menus,
        'current_menu': current_menu,
    }
    return render(request, 'categories.html', context)

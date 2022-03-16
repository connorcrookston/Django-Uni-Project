from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Page

def index(request):
    # Construct a dictionary to pass to the template engine as its context
    # note the key boldmessage matches to {{ boldmessage }} in the template!

    category_list = Category.objects.order_by('-likes')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list

    # return a rendered response to send to the client
    # we make use of the shortcut function to make our lives easier
    # note that the first parameter is the tempate we wish to use
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    context_dict = {'name': 'Connor'}
    return render(request, 'rango/about.html', context=context_dict)


def show_category(request, category_name_slug):
    context_dict = []

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category

    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context=context_dict)



from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import Http404
from tea.models import *
from tea.forms import *


def view_categories(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})


def view_category(request, id):
    category = get_object_or_404(Category, id=id)
    return render(request, 'category.html', {'category': category})


def view_products(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


# class BookView(ListView)


def view_orders(request):
    orders = Order.objects.all()
    return render(request, 'orders.html', {'orders': orders})

"""
def details(request, id):
    if request.method == 'GET':
        return render_to_response('index.html', {'form': BookForm()})
    elif request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
"""

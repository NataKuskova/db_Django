from django.shortcuts import redirect
from django.http import HttpResponseRedirect, request
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.views.generic.base import View
from django.contrib import admin
from tea.models import *
from tea.forms import *


class ProductsList(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'
    paginate_by = 5

    def get_queryset(self):
        queryset = super(ProductsList, self).get_queryset()
        search = self.request.GET.get('search', None)
        sort = self.request.GET.get('sort', None)
        by = self.request.GET.get('by', None)
        if search is not None and sort is not None:
            return queryset.filter(Q(name__icontains=search) |
                                   Q(price__icontains=search) |
                                   Q(quantity__icontains=search)
                                   ).order_by(by + sort)
        if search is not None:
            return queryset.filter(Q(name__icontains=search) |
                                   Q(price__icontains=search) |
                                   Q(quantity__icontains=search))
        if sort is not None:
            return queryset.order_by(by + sort)
        return queryset


class ProductDetail(DetailView):
    model = Product
    pk_url_kwarg = 'id'
    template_name = 'product.html'


class ProductCreate(CreateView):
    model = Product
    template_name = 'edit_product.html'
    fields = ['name', 'category', 'price', 'quantity', 'photo']
    success_url = reverse_lazy('products_list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect(self.get_success_url())


class ProductDelete(DeleteView):
    model = Product
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('products_list')


class ProductUpdate(UpdateView):
    model = Product
    pk_url_kwarg = 'id'
    template_name = 'edit_product.html'
    fields = ['name', 'category', 'price', 'quantity', 'photo']


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/tea/login/"
    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = "/tea/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/tea/")


class BuyerCreate(FormView):
    template_name = 'edit_user.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('products_list')

    def form_valid(self, form):
        self.object = form.save()
        return redirect(self.get_success_url())

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from .forms import ProductForm
from catalog.models import Product, Category


class HomeListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'


class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = form = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:index')
    context_object_name = 'product'

    def form_valid(self, form):
        form.instance.owner = self.request.user  # ← вот здесь мы указываем текущего пользователя
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:index')
    context_object_name = 'product'

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner or user.has_perm('catalog.can_change_product'):
            return ProductForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:index')
    context_object_name = 'product'


    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner or user.has_perm('catalog.can_delete_product'):
            return ProductForm
        raise PermissionDenied


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product.html'
    success_url = reverse_lazy('catalog:index')
    context_object_name = 'product'


class UnpublishProductView(LoginRequiredMixin, View):
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)

        if not request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden("У вас нет прав для отмены публикации продукта.")

        product = True
        product.save()

        return redirect('catalog:product_detail', pk=product.id)

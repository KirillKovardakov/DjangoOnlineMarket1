from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,TemplateView,DetailView

from catalog.models import Product,Category


class HomeListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name='products'

class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'
    context_object_name='product'

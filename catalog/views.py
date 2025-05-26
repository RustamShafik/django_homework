from django.shortcuts import render, get_object_or_404
from catalog.models import Product
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView


# def contacts(request):
#     return render(request, "contacts.html")
class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"

class ProductListView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product


# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {"product": product}
#     return render(request, 'product_detail.html', context)



from django.shortcuts import render, get_object_or_404
from catalog.models import Product
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from .forms import ProductForm, ProductModeratorForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


# def contacts(request):
#     return render(request, "contacts.html")
class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"

class ProductListView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy('catalog:products_list')

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy('catalog:products_list')

    def get_form_class(self):
        user = self.request.user
        if user.has_perm("catalog.can_unpublish_product") and user.has_perm("catalog.delete_product"):
            return ProductModeratorForm
        return ProductForm

class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy('catalog:products_list')
    permission_required = 'catalog.delete_product'
    raise_exception = True


# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {"product": product}
#     return render(request, 'product_detail.html', context)



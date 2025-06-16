from django.shortcuts import render, get_object_or_404
from catalog.models import Product
from .services import ProductService
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

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

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

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        user = self.request.user
        if obj.owner != user and not (
                user.has_perm("catalog.can_unpublish_product") and user.has_perm("catalog.delete_product")):
            raise PermissionDenied
        return obj

class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy('catalog:products_list')
    permission_required = 'catalog.delete_product'
    raise_exception = True

    def has_permission(self):
        obj = self.get_object()
        user = self.request.user
        return obj.owner == user or user.has_perm(self.permission_required)

class ProductByCategoryView(ListView):
    model = Product
    template_name = "catalog/products_by_category.html"
    context_object_name = "products"

    def get_queryset(self):
        category_id = self.kwargs.get("category_id")
        return ProductService.get_products_list_by_category(category_id)


# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {"product": product}
#     return render(request, 'product_detail.html', context)



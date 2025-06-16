from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ContactsView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView
from django.views.decorators.cache import cache_page

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name='products_list'),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("products/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="product_detail"),
    path("products/new/", ProductCreateView.as_view(), name='product_create'),
    path("products/update/<int:pk>/", ProductUpdateView.as_view(), name='product_update'),
    path("products/delete/<int:pk>/", ProductDeleteView.as_view(), name='product_delete'),
]

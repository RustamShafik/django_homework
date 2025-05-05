from django.contrib import admin

from catalog.models import Category, Product


# Зарегистрируйте модели Product и Category в админке.
# Настройте отображение для моделей: Для Category выведите id и name
# в списке. Для Product выведите id , name , price и category в списке.
# Настройте фильтрацию продуктов по категории. Настройте поиск
# по полям name и description .


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "purchase_price",
        "category",
    )
    list_filter = ("category",)
    search_fields = ("name", "description")

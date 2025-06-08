from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Add test products to database"

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category, _ = Category.objects.get_or_create(
            name="Гаджеты и аксессуары",
            description="Категория для различных гаджетов и аксессуаров",
        )
        products = [
            {
                "name": "Смарт-часы Apple Watch Series 8",
                "purchase_price": 32900.00,
                "category": category,
            },
            {
                "name": "Беспроводные наушники AirPods Pro 2",
                "purchase_price": 24900.00,
                "category": category,
            },
            {
                "name": "Bluetooth колонка JBL Flip 5",
                "purchase_price": 8990.00,
                "category": category,
            },
            {
                "name": "Портативный аккумулятор Anker PowerCore 10000",
                "purchase_price": 2299.00,
                "category": category,
            },
            {
                "name": "Умный термостат Google Nest",
                "purchase_price": 12990.00,
                "category": category,
            },
            {
                "name": "Камера видеонаблюдения Xiaomi Mi Home Security Camera 360",
                "purchase_price": 3990.00,
                "category": category,
            },
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully added product: {product.name}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Product already exists: {product.name}")
                )

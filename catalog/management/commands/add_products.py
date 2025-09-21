from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Add test products to the database'

    def handle(self, *args, **kwargs):
        Category.objects.all().delete()
        Product.objects.all().delete()
        category1, _ = Category.objects.get_or_create(name='Телефон', description='Гаджеты, андроиды, яблочные устройства')
        category2, _ = Category.objects.get_or_create(name='Бытовая утварь', description='Предметы для использования дома')

        products = [
            {'name': 'Айпфон', 'description': 'Как iphone16 только круче', 'category': category1, 'price': '1000000'},
            {'name': 'Самсунг', 'description': 'Как Айпфон только круче', 'category': category1, 'price': '100000'},
            {'name': 'Грабли', 'description': 'Удобно подметать пол', 'category': category2, 'price': '1000'},
            {'name': 'Веник', 'description': 'Удобно собирать траву', 'category': category2, 'price': '100'},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product.name}'))

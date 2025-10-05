from django import forms
from django.core.exceptions import ValidationError

from .models import Product


# class CategoryForm(forms.ModelForm):
#     model = Category
#     fields = ['name', 'description']
#
#     def __init__(self, *args, **kwargs):
#         super(CategoryForm, self).__init__(*args, **kwargs)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        # Настройка атрибутов виджета для полей
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placedescriptionholder': 'Введите название товара'  # Текст подсказки внутри поля
        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите описание'  # Текст подсказки внутри поля
        })
        self.fields['category'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите категорию'  # Текст подсказки внутри поля
        })
        self.fields['price'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите цену'  # Текст подсказки внутри поля
        })

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if int(price) < 0:
            raise ValidationError('Цена не может быть отрицательной')
        return price

    def clean_name(self):
        forbidden_words = ['казино', 'биржа', 'обман', 'криптовалюта', 'дешево', 'полиция', 'крипта', 'бесплатно',
                           'радар']
        name = self.cleaned_data.get('name')
        if name and name.lower() in forbidden_words:
            raise ValidationError('Имя содержит запрещённые слова')
        return name

    def clean_description(self):
        forbidden_words = ['казино', 'биржа', 'обман', 'криптовалюта', 'дешево', 'полиция', 'крипта', 'бесплатно',
                           'радар']
        description = self.cleaned_data.get('description')
        if description and description.lower() in forbidden_words:
            raise ValidationError('Описание содержит запрещённые слова')
        return description

from django import forms
from .models import Product
from django.core.exceptions import ValidationError

FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'photo', 'description', 'category', 'purchase_price']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите название товара'})
        self.fields['photo'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Загрузите фото товара'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите описание товара'})
        self.fields['category'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Укажите категорию товара'})
        self.fields['purchase_price'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите цену товара'})


    def clean_purchase_price(self):
        product_price = self.cleaned_data.get('purchase_price')
        if product_price is not None and product_price < 0:
            raise ValidationError('Цена не может быть отрицательной')
        return product_price

    def clean(self):
        cleaned_data = super().clean()
        product_name = cleaned_data.get('name') or ''
        product_description = cleaned_data.get('description') or ''

        for word in FORBIDDEN_WORDS:
            if word.lower() in product_name.lower():
                self.add_error('name', 'Это слово использовать нельзя')
            if word.lower() in product_description.lower():
                self.add_error('description', 'Это слово использовать нельзя')


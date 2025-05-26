from django import forms
from .models import Product
from django.core.exceptions import ValidationError

FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'photo', 'description', 'category', 'purchase_price']

    def clean(self):
        cleaned_data = super().clean()
        product_name = cleaned_data.get('name') or ''
        product_description = cleaned_data.get('description') or ''

        for word in FORBIDDEN_WORDS:
            if word.lower() in product_name.lower():
                self.add_error('name', 'Это слово использовать нельзя')
            if word.lower() in product_description.lower():
                self.add_error('description', 'Это слово использовать нельзя')


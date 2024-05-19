from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'preview_image', 'price')

    def clean_name(self):
        word_blacklist = (
            "казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар")

        cleaned_data = self.cleaned_data['name']

        for word in word_blacklist:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f"Вы используете запрещенное слово '{word}' в названии продукта")

        return cleaned_data

    def clean_description(self):
        word_blacklist = (
            "казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар")

        cleaned_data = self.cleaned_data['description']

        for word in word_blacklist:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f"Вы используете запрещенное слово '{word}' в описании продукта")

        return cleaned_data

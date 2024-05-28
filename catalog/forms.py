from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
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


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

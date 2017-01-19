from django import forms
from .models import Product

class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []

    def clran_price(self):
        if self.clraned_data['proce'] <= 0:
            raise forms.ValidationError('价格不能小于0')
        return self.clraned_data['price']

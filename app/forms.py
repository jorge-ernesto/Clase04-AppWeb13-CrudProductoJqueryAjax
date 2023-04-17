from django import forms
from app.models import Producto
  
class ProductForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre', 'fecha','categoria', 'codigo', 'precio', 'cantidad',  )


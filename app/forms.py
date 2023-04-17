from django import forms
from app.models import Producto
  
# El formulario hereda las validaciones definidas en el modelo.
class ProductForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre', 'fecha','categoria', 'codigo', 'precio', 'cantidad',  )

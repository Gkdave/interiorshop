from django.forms import ModelForm 

from shop.product.models import Product 

class ProductForm(ModelForm):
    class Meta:
        model = Product 
        fields = [
            'category', 'image','title', 'description','price'
        ]
        
    
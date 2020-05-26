from django.db import models

# Create your models here.
from django.forms import ModelForm, Select, TextInput, FileInput

from product.models import Product

#burası formmumuzun olduğu yer
class AddProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category','title','keywords','description','image','price','ili','detail','slug','metrekare','binayasi','kati','banyosayisi','balkonsayisi','esyali','aidat','depozito','odasayisi']#buraya eklenecekler
        widgets = {
            'category': Select(attrs={'class': 'form-control', 'placeholder': 'category'}, ),
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'title'}),
            'keywords': TextInput(attrs={'class': 'form-control', 'placeholder': 'keywords'}),
            'description': TextInput(attrs={'class': 'form-control', 'placeholder': 'description'}),
            'image': FileInput(attrs={'class': 'form-control', 'placeholder': 'image'}),
            'price': TextInput(attrs={'class': 'form-control', 'placeholder': 'price'}),
            'ili': TextInput(attrs={'class': 'form-control', 'placeholder': 'ili'}),
            'detail': TextInput(attrs={'class': 'form-control', 'placeholder': 'detail'}),
            'slug': TextInput(attrs={'class': 'form-control', 'placeholder': 'slug'}),
            'metrekare': TextInput(attrs={'class': 'form-control', 'placeholder': 'metrekare'}),
            'binayasi': TextInput(attrs={'class': 'form-control', 'placeholder': 'binayasi'}),
            'kati': TextInput(attrs={'class': 'form-control', 'placeholder': 'kati'}),
            'banyosayisi': TextInput(attrs={'class': 'form-control', 'placeholder': 'banyosayisi'}),
            'esyali': Select(attrs={'class': 'form-control', 'placeholder': 'esyali'}),
            'aidat': TextInput(attrs={'class': 'form-control', 'placeholder': 'aidat'}),
            'balkonsayisi': TextInput(attrs={'class': 'form-control', 'placeholder': 'balkonsayisi'}),
            'depozito': TextInput(attrs={'class': 'form-control', 'placeholder': 'depozito'}),
            'odasayisi': TextInput(attrs={'class': 'form-control', 'placeholder': 'odasayisi'}),
        }
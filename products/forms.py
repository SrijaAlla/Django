from django import forms
from .models import Product, Category, Review

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

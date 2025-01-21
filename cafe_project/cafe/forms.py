from django import forms
from .models import Review, MenuItem, CarouselItem

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']  # Add any fields you want to include in the form


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'category', 'price', 'description', 'image']
        
class CarouselItemForm(forms.ModelForm):
    class Meta:
        model = CarouselItem
        fields = ['name', 'description', 'image']
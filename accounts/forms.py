from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from marketplace.models import Item


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_buyer', 'is_seller', 'is_business')


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['make', 'year', 'model_name', 'model_designation', 'category', 'title', 'description', 'price']

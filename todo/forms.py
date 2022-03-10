from django import forms
from .models import Item


# Inherit all the functionality of forms.ModelForm
class ItemForm(forms.ModelForm):
    # To tell the form which model it's going to be associated with
    # Which fields it should render, how it should display error messages, etc.
    class Meta:
        model = Item
        fields = ['name', 'done']
from django import forms
from cardapio_virtual.models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"
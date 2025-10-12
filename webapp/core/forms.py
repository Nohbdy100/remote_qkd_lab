from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    item_name = forms.ModelChoiceField(
        label="Camera Rotation",
        queryset=Item.objects.all(),
        required=True
    )

    class Meta:
        model = Item
        fields = ['item_name']
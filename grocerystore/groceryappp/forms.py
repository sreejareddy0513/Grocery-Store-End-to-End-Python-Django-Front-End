from django import forms
from models import Grocery
class Grocery_form(forms.ModelForm):
    class Meta:
        model=Grocery
        exclude=['Amount',]
from django import forms

class AddItemForm(forms.Form):
    name=forms.CharField(max_length=30)
    quantity=forms.IntegerField()
    
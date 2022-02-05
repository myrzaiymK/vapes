from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'phone' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'message' : forms.Textarea(attrs={'class':'form-control'}),
        }
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1,21)]
class CartAddProductForm(forms.ModelForm):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int)

    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)



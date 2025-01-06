from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
#? ceque permet de faire la classe Meta
    class Meta:
        model = Contact  
        fields = ['name', 'prenom','telephone','email']
from django import forms
from .models import Contact

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    prenom = forms.CharField(max_length=50)
    telephone = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=254)

    def save_contact(self):
        contact = Contact(
            name = self.name,
            prenom = self.prenom,
            telephone = self.telephone,
            email = self.email
        )
        contact.save()
        print(f"Contact enregistrez avec succès, Alhamdulilah")
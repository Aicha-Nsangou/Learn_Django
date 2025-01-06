from django.db import models

# Create your models here

class Contact(models.Model):

    name = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return (f"ID:{self.id}\n name : {self.name}\n prenom : {self.prenom}\n telephone: {self.telephone} \n email:{self.email}")
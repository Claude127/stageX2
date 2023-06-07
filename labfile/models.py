from django.db import models
from django.contrib.auth.hashers import check_password as django_check_password

# Create your models here.


class Action(models.Model):
    nom = models.CharField(max_length=25)

    def __str__(self):
        return self.nom


class Role(models.Model):
    nom = models.CharField(max_length=15)
    actions = models.ManyToManyField(Action)

    def __str__(self):
        return self.nom


class Utilisateur(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=25)
    email = models.EmailField(max_length=60)
    password = models.CharField(max_length=8)
    image = models.FileField(upload_to='phots', null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom






class Document(models.Model):
    nom = models.CharField(max_length=30)
    categorie = models.CharField(max_length=30, null=True)
    emplacement = models.FileField(upload_to='fichiers')
    date_creation = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

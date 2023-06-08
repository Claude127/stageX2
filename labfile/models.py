from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .manager import CustomAccountManager


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


class Utilisateur(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    nom = models.CharField(max_length=30, unique=True)
    prenom = models.CharField(max_length=25)
    image = models.FileField(upload_to='phots', null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    date_creation = models.DateField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['nom', 'prenom']

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

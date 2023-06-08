from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _



class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, nom, prenom, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Super user must have is staff true')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super user must have is superuser true')

        return self.create_user(email, nom, prenom, password, **extra_fields)

    def create_user(self, email, nom, prenom, password, **extra_fields):
        if not email:
            raise ValueError(_('Email is required'))

        email = self.normalize_email(email)
        user = self.model(email=email, nom=nom, prenom=prenom, **extra_fields)
        user.set_password(password)
        user.save()
        return user

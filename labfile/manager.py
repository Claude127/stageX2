from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _




class CustomAccountManager(BaseUserManager):

    def create_user(self, email, nom, prenom, password=None, **extra_fields):
        if not email:
            raise ValueError(_('Email is required'))

        email = self.normalize_email(email)
        user = self.model(email=email, nom=nom, prenom=prenom, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, nom, prenom, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        user = self.create_user(
            email=self.normalize_email(email),
            nom=nom,
            prenom=prenom,
            password=password,
            **extra_fields)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Super user must have is staff true')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super user must have is superuser true')
        user.save(using=self._db)

        return user


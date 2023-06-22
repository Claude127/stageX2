
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Utilisateur
from django.core.mail import send_mail
from django.conf import settings


@receiver(post_save, sender=Utilisateur)
def send_email_on_create(sender, instance, created, **extra_fields):
    if created:
        subject = 'Bienvenue à LAB2VIEW'
        message = f'Bienvenue {instance.prenom},\n\n L\'équipe de LAB2VIEW est heureuse de vous compter ' \
                  f'parmi ses effectifs :) \nCi-joint vos identifiants pour l\'accès à Labfile : Notre application de ' \
                  f'stockage de documents \n\n Lien de connexion : localhost:8000 \n Email :{instance.email} \n Mot ' \
                  f'de passe (par défaut) : labf!le123 \n\nNB: le mot de passe doit etre modifié après la prémière ' \
                  f'connexion!   \n\nCordialement,\nL\'équipe de LAB2VIEW'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [instance.email, ]
        send_mail(subject, message, email_from, recipient_list)

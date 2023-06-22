
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Utilisateur
from django.core.mail import send_mail
from django.conf import settings


@receiver(post_save, sender=Utilisateur)
def send_email_on_create(sender, instance, created, **extra_fields):
    if created:
        subject = 'Bienvenue sur notre site'
        message = f'Bonjour {instance.prenom},\n\nBienvenue sur notre site !\n\nCordialement,\nL\'équipe de notre site'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [instance.email, ]
        send_mail(subject, message, email_from, recipient_list)

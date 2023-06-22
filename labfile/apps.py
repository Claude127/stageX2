from django.apps import AppConfig


class LabfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'labfile'

    def ready(self):
        import labfile.signals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea

from .models import Utilisateur, Role, Action, Document


class UserAdminConfig(admin.ModelAdmin):
    list_display = ('email', 'nom', 'prenom', 'role', 'is_active', 'is_staff')
    search_fields = ('email', 'role', 'nom', 'prenom',)
    ordering = ('date_creation',)
    list_filter = ('email', 'role', 'is_active', 'is_staff')


class DocumentAdmin(admin.ModelAdmin):
    list_display =  ('nom', 'categorie')
    search_fields = ('nom', 'categorie')
    ordering = ('nom', 'categorie')
    list_filter = ('nom', 'categorie')


# # custom
# admin.site.index_template = 'admin/dashboard.html',
# Register your models here.
admin.site.register(Utilisateur, UserAdminConfig)
admin.site.register(Role)
admin.site.register(Action)
admin.site.register(Document, DocumentAdmin)

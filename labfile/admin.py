from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea

from .models import Utilisateur, Role, Action, Document


class UserAdminConfig(UserAdmin):
    search_fields = ('email', 'role', 'nom', 'prenom',)
    list_filter = ('email', 'role', 'is_active', 'is_staff')
    ordering = ('date_creation',)
    list_display = ('email', 'nom', 'prenom', 'role', 'is_active', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'nom', 'prenom', 'image', 'role',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),

    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nom', 'prenom', 'image', 'role', 'password1', 'password2', 'is_active', 'is_staff')
        }

         )
    )


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

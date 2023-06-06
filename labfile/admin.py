from django.contrib import admin

from .models import Utilisateur, Role, Action, Document

# Register your models here.

admin.site.register(Utilisateur)
admin.site.register(Role)
admin.site.register(Action)
admin.site.register(Document)

# # custom
# admin.site.index_template = 'admin/dashboard.html',

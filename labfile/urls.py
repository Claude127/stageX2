from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.urls import path, re_path
from django.views.static import serve

from . import dashboard
from .views import file, dashboard, user_admin, profile, add_file, file_mod, profile_mod, login_user, logout_user, \
    search, delete_file, sort_files

urlpatterns = [
    # utiliser pour charger les fichiers media une fois le debug =false
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

    # gestion des fichiers
    # page pour voir les fchiers
    path('files/', file, name='file'),
    # page pour ajouter un fichier
    path('add_file/', add_file, name='add_file'),
    # page pour voir un fichier
    path('delete_file/<int:file_id>/', delete_file, name='delete_file'),
    # page pour modifier un fichier
    path('file_mod/<int:file_id>/', file_mod, name='file_mod'),
    # page pour afficher des produits par categorie
    path('sort_files/<int:category_id>/', sort_files, name='sort_files'),
    # page pour voir le dashboard
    path('dashboard', dashboard, name='dashboard'),

    # gestion des profils
    # page pour voir le profil
    path('profil/', profile, name='profile'),
    # page pour modifier le profil
    path('profile_mod/', profile_mod, name='profile_mod'),

    # account_user
    # page pour se connecter
    path('login/', login_user, name='login'),
    path('', file, name='login'),
    # page pour se deconnecter
    path('logout/', logout_user, name='logout'),

    # rechercher des fichiers
    path('search/', search, name='search-file'),
    path('users/', user_admin, name='user_admin'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

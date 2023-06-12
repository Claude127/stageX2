from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import file, dashboard, user_admin, profile, add_file, view_file, file_mod, profile_mod, \
    login_user, logout_user, search

urlpatterns = [

    #gestion des fichiera
        #page pour voir les fchiers
        path('files/', file, name='file'),
        #page pour ajouter un fichier
        path('add_file/', add_file, name='add_file'),
        #page pour voir un fichier
        path('view-file/<int:file_id>/', view_file, name='view-file'),
        #page pour modifier un fichier
        path('file_mod/', file_mod, name='file_mod'),
        #page pour voir le dashboard
        path('dashboard/', dashboard, name='dashboard'),

    #gestion des profils
        #page pour voir le profil
        path('profil/', profile, name='profile'),
        #page pour modifier le profil
        path('profile_mod/', profile_mod, name='profile_mod'),

    # account_user
        # page pour se connecter
        path('login/', login_user, name='login'),
        path('', login_user, name='login'),
        # page pour se deconnecter
        path('logout/', logout_user, name='logout'),

    #rechercher des fichiers
    path('search/', search, name='search-file'),
    path('users/', user_admin, name='user_admin'),




]



if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

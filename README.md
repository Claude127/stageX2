# stageX2
Mise en place d'une application de visualisation de performances et gestion d'entreprise.
son but est de permettre la visualisation de l'évolution des activités d'une entreprise,
ainsi que de permettre la gestion de fichiers(accès et opérations):

### Prerequis 
l'application est concue en **python** à l'aide du framework **DJANGO**.Il utilise également 
d'autres librairies.l'ensemble de ces dernières sont disponibles dans le fichier d'emplacement**app_dash/requirements.txt**.

### Installation 
Après avoir installé tous les packages présents dans le fichier *requirements.txt*:
1. Configurer vos variables d'environnement en modifiant le fichier **.env_sample**. Insérez-y les paramètres de configurations de votre base de données (préalablement crée)
2. Dans le terminal , effectuez les migrations à l'aide de la commande **py manage.py migrate**
3. Lancer le projet à l'aide de la commande **py manage.py runserver**.

NB: Assurez d'etre dans le dossier du projet contenant le fichier **manage.py**

Pour accéder à la partie utilisateur : 
1. Créer un super utilisateur à l'aide de la commande **py manage.py createsuperuser**
2. Entrer les informations sollicitées et puis lancer l'application . vous accéderez à la partie admin en ajoutant **/admin/** à la fin de,l'url de navigation 



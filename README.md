# stageX2
## App for Visualization of Performances and Company Management

This app is meant to visualize the fluctuations in the company activities and allow files management (access and operations).

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Run `docker compose up --remove-orphans`.
2. In another shell, run `docker exec -it labfile-app sh`.
3. Inside the shell, run `python3 manage.py migrate`.
4. Run `python3 manage.py seed labfile --number=15`. This command will help you populate the database to start using the app
5. You can use that interactive shell to make other tests.

Pour accéder à la partie utilisateur : 
1. Créer un super utilisateur à l'aide de la commande **py manage.py createsuperuser**
2. Entrer les informations sollicitées et puis lancer l'application . vous accéderez à la partie admin en ajoutant **/admin/** à la fin de,l'url de navigation 

## STACK

This app is built with the following technologies:

- [Django](https://www.djangoproject.com/)
- [Django Dash](https://django-plotly-dash.readthedocs.io/en/latest/)
- [Plotly](https://plotly.com/)
- [Pandas](https://pandas.pydata.org/)
- [MySQL](https://www.mysql.com/)  


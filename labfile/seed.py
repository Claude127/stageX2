from random import random

from django_seed import Seed

seeder = Seed.seeder()

from .models import Categorie

seeder.add_entity(Categorie, 5, {
    'nom': lambda x: random.choice(['Juridiques', 'Comptabilites', 'Rapport', 'Formation', 'Livrables'])
})

seeder.execute()

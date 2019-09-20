# OPenClassRooms - Projet #7
## Creer GrandPy bot, le papy robot


Ah, les grands-pères... Je ne sais pas vous, mais le mien connaissait quantité d'histoires. Il me suffisait de lui dire un mot pour le voir parti pendant des heures. "Tu veux l'adresse de la poste ? Ah oui, c'est bien. Mais je t'ai déjà raconté que j'ai aidé à la construire ? C'était en 1974 et..." 😴

Pourtant, j'adore ses récits ! J'ai beaucoup appris et rêvé d'autres contrées en l'écoutant. Voici donc le projet que je vous propose : créer un robot qui vous répondrait comme votre grand-père ! Si vous lui demandez l'adresse d'un lieu, il vous la donnera, certes, mais agrémentée d'un long récit très intéressant. Vous êtes prêt·e ?

#### Install
###### Clone
```
git clone https://github.com/Azer1338/GrandPy_bot.git
```

###### Init virtualenv
```
cd GrandPy
virtualenv --python=python3 venv
```

###### Install requirements
```
. venv/bin/activate
pip install -r requirements.txt
```

###### Set Google Maps KEY
```
You need to insert your api key in config.py:
GOOGLE_MAPS_KEY = 'XXXX'
```

###### Test
```
pytest GrandPy_BotApp/
```

###### Run
```
python3 run.py
```

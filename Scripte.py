import pymongo
import json
from pprint import pprint
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.startest
ships = db.ships

print('connection !')

db.ships.drop()

with open('vaisseau.json') as f:
    file_data = json.load(f)

ships.insert_one(file_data)

allships = ships.find()
print("Tout les vaisseaus!")
for ship in allships:
    pprint(ship)

#    db.ships.aggregate([
#    {$match: {"vaisseau.constructeur": "AEGIS"}},
#    {$project: {
#        vaisseau: {$filter: {
#            input: '$vaisseau',
#            as: 'nom',
#            cond: {$eq: ['$$nom.constructeur', 'AEGIS']}
#        }},
#        _id: 0
#    }}
#])

#pipeline = [{"vaisseau.constructeur": "AEGIS"}]
#db.ships.aggregate(pipeline)

import pymongo
import json
from pprint import pprint
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.startest
ships = db.ship

print('connection !')

db.ship.drop()

#with open('vaisseau.json') as f:
#    file_data = json.load(f)
#
#ships.insert_one(file_data)

vaisseauxlist = [
    {
     "nom": "F7C HORNET",
     "constructeur": "Anvil Aerospace",
     "hauteur": 22,
     "largeur": 6,
     "masse" : 73535,
     "role": "Combat",
     "prix": 150
        },
      {
     "nom": "CONSTELLATION AQUILA",
     "constructeur": "RSI",
     "hauteur": 61,
     "largeur": 14,
     "masse" : 439108,
     "role": "Exploration",
     "prix": 372
        },
    {
     "nom": "AURORA ES",
     "constructeur": "RSI",
     "hauteur": 18,
     "largeur": 4,
     "masse" : 25172,
     "role": "Transport",
     "prix": 24
        },
    {
     "nom": "MANTIS",
     "constructeur": "RSI",
     "hauteur": 30,
     "largeur": 8,
     "masse" : 225621,
     "role": "Combat",
     "prix": 180
        },
    {
     "nom": "CONSTELLATION TAURUS",
     "constructeur": "RSI",
     "hauteur": 61,
     "largeur": 14,
     "masse" : 416009,
     "role": "Transport",
     "prix": 180
        },
    {
     "nom": "CONSTELLATION AQUILA",
     "constructeur": "RSI",
     "hauteur": 61,
     "largeur": 14,
     "masse" :439108,
     "role": "Exploration",
     "prix": 372
        },
    {
     "nom": "CONSTELLATION ANDROMEDA",
     "constructeur": "RSI",
     "hauteur": 61,
     "largeur": 14,
     "masse" :419850,
     "role": "Transport",
     "prix": 330
        },
    {
     "nom": "3001",
     "constructeur": "Origin",
     "hauteur": 27,
     "largeur": 8,
     "masse" : 66320,
     "role": "Transport",
     "prix": 72
        },
    {
     "nom": "CUTLASS BLACK",
     "constructeur": "Drake",
     "hauteur": 29,
     "largeur": 10,
     "masse" : 226700,
     "role": "Combat",
     "prix": 138
        },
    {
     "nom": "AVENGER TITAN",
     "constructeur": "AEGIS",
     "hauteur": 22,
     "largeur": 5,
     "masse" : 50056,
     "role": "Transport",
     "prix": 84
        },
    {
     "nom": "GLADIUS",
     "constructeur": "AEGIS",
     "hauteur": 20,
     "largeur" : 5,
     "masse" : 48958,
     "role": "Combat",
     "prix": 108
        },
    {
     "nom": "TERRAPIN",
     "constructeur": "Anvil Aerospace",
     "hauteur": 19,
     "largeur" : 6,
     "masse" :86454,
     "role": "Combat",
     "prix": 1320
        },
    {
     "nom": "CARRACK EXPEDITION",
     "constructeur": "Anvil Aerospace",
     "hauteur": 126,
     "largeur": 36,
     "masse" : 4397858,
     "role": "Exploration",
     "prix": 1320
        },
    {
     "nom": "ARROW",
     "constructeur": "Anvil Aerospace",
     "hauteur": 16,
     "largeur": 4,
     "masse" : 30752,
     "role": "Combat",
     "prix": 108
        },
   {
     "nom": "REDEEMER",
     "constructeur": "AEGIS",
     "hauteur": 37,
     "largeur": 11,
     "masse" : 120380,
     "role": "Combat",
     "prix": 530
         },
   {
     "nom": "JAVELIN",
     "constructeur": "AEGIS",
     "hauteur": 480,
     "largeur": 72,
     "masse" : 109860179,
     "role": "Combat",
     "prix": 1240
         },
   {
     "nom": "NAUTILUS",
     "constructeur": "AEGIS",
     "hauteur": 125,
     "largeur": 21,
     "masse" : 34567,
     "role": "Combat",
     "prix": 1240
         },
   {
     "nom": "VULCAN",
     "constructeur": "AEGIS",
     "hauteur": 38,
     "largeur": 10,
     "masse" : 625330,
     "role": "Transport",
     "prix": 134
         },
   {
     "nom": "X1 BASE",
     "constructeur": "ORIGIN",
     "hauteur": 5,
     "largeur": 1,
     "masse" : 1610,
     "role": "Transport",
     "prix": 50
         },
      {
     "nom": "HAWK",
     "constructeur": "Anvil Aerospace",
     "hauteur": 17,
     "largeur": 6,
     "masse" : 40000,
     "role": "Combat",
     "prix": 650
         },
   {
     "nom": "CRUCIBLE",
     "constructeur": "Anvil Aerospace",
     "hauteur": 90,
     "largeur": 20,
     "masse" : 3650500,
     "role": "Transport",
     "prix": 1800
         },
   {
     "nom": "VALKYRIE",
     "constructeur": "Anvil Aerospace",
     "hauteur": 38,
     "largeur": 9,
     "masse" : 56000,
     "role": "Combat",
     "prix": 650
         },
   {
     "nom": "POLARIS",
     "constructeur": "RSI",
     "hauteur": 155,
     "largeur": 35,
     "masse" : 17155000,
     "role": "Combat",
     "prix": 1790
         },
   {
     "nom": "ORION",
     "constructeur": "RSI",
     "hauteur": 170,
     "largeur": 50,
     "masse" : 26496000,
     "role": "Transport",
     "prix": 780
         },
   {
     "nom": "HERALD",
     "constructeur": "Drake",
     "hauteur": 23,
     "largeur": 9,
     "masse" : 64001,
     "role": "Transport",
     "prix": 650
         },
   {
     "nom": "CORSAIR",
     "constructeur": "Drake",
     "hauteur": 55,
     "largeur": 31,
     "masse" : 45000,
     "role": "Exploration",
     "prix": 780
         },
   {
     "nom": "VULTURE",
     "constructeur": "DRAKE",
     "hauteur": 33,
     "largeur": 9,
     "masse" : 55000,
     "role": "Transport",
     "prix": 549
         },
   {
     "nom": "CATERPILLAR",
     "constructeur": "Drake",
     "hauteur": 111,
     "largeur": 13,
     "masse" : 1608205,
     "role": "Transport",
     "prix": 1200
         },
   {
     "nom": "KRAKEN",
     "constructeur": "Drake",
     "hauteur": 270,
     "largeur": 64,
     "masse" : 37000,
     "role": "Combat",
     "prix": 1450
         },
   {
     "nom": "ECLIPSE",
     "constructeur": "AEGIS",
     "hauteur": 20,
     "largeur": 4,
     "masse" : 54216,
     "role": "Combat",
     "prix": 490
         }
]

try:
    ships.insert_many(vaisseauxlist)
except:
    print("Erreur Insertion")

allships = ships.find()
print("Tout les vaisseaus!")
for ship in allships:
    pprint(ship)

Originship = db.ship.find({'constructeur': 'Origin'})
print("vaisseaux Origin!")
for ship in Originship:
    pprint(ship)

combatship = db.ship.find({"role": "Combat"})
print("vaisseaux de COmbat!")
for ship in combatship:
    pprint(ship)

combatshipsaegis = db.ship.find({'constructeur': 'AEGIS', "role": "Combat"})
print("vaisseaux AEGIS de combat!")
for ship in combatshipsaegis:
    pprint(ship)

transportships = db.ship.find({"role": "Transport", "prix": {"$lte": 100 }})
print("vaisseaux de transport pas chère!")
for ship in transportships:
    pprint(ship)

Combatship = db.ship.find({"role": "Combat", "prix": {"$gte": 100, "$lte": 300 }})
print("vaisseaux de combat moyen!")
for ship in Combatship:
    pprint(ship)

def findConstructeur(constructeur):
    Constructeurship = db.ship.find({'constructeur': constructeur})
    print("vaisseaux : " + constructeur)
    for ship in Constructeurship:
        pprint(ship)

def findCombat():
    combatship = db.ship.find({"role": "Combat"})
    print("vaisseaux de Combat!")
    for ship in combatship:
        pprint(ship)
    
def findTransport():
    transportship = db.ship.find({"role": "Transport"})
    print("vaisseaux de Transport!")
    for ship in transportship:
        pprint(ship)

def findExploration():
    Explorationship = db.ship.find({"role": "Exploration"})
    print("vaisseaux d'Exploration'!")
    for ship in Explorationship:
        pprint(ship)

def findBudget(minimum, maximum):
    Budgetship = db.ship.find({"prix": {"$gte": minimum, "$lte": maximum }})
    print("vaisseaux dans votre budget!")
    for ship in Budgetship:
        pprint(ship)

def findPerfect(role, minimum, maximum):
    Budgetship = db.ship.find({"role": role, "prix": {"$gte": minimum, "$lte": maximum }})
    print("vaisseaux dans votre budget!")
    for ship in Budgetship:
        pprint(ship)
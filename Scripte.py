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

db.ships.find().sort({"nom":-1}).pretty()

client.close()

aegisships = db.ships.find({},{"constructeur": "AEGIS"})
print("vaisseaux AEGIS!")
for ship in aegisships:
    pprint(ship)


    db.ships.aggregate([
    {$match: {"vaisseau.constructeur": "AEGIS"}},
    {$project: {
        vaisseau: {$filter: {
            input: '$vaisseau',
            as: 'nom',
            cond: {$eq: ['$$nom.constructeur', 'AEGIS']}
        }},
        _id: 0
    }}
])

pipeline = [{"vaisseau.constructeur": "AEGIS"}]
db.ships.aggregate(pipeline)
from connect_mongo import *


mycol = mydb["customers"]

mylist = [
    {"name": "Petr", "surname": "Novák", "address": "Hlavní 22, Brno"},
    {"name": "Radek", "surname": "Svoboda", "address": "Jarní 5, Ostrava"},
    {"name": "Jana", "surname": "Novotná", "address:": "Pardobická 14, Praha"}
]

response = mycol.insert_many(mylist)

print(response.inserted_ids)

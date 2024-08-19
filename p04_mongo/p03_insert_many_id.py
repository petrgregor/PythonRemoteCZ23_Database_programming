from connect_mongo import *


mycol = mydb["customers"]

mylist = [
    {"_id": 1, "name": "Petr", "surname": "Novák", "address": "Hlavní 22, Brno"},
    {"_id": 2, "name": "Radek", "surname": "Svoboda", "address": "Jarní 5, Ostrava"},
    {"_id": 3, "name": "Jana", "surname": "Novotná", "address:": "Pardubická 14, Praha"},
    {"_id": 4, "surname": "Blatný", "phone_number": "+420777123456"},
    {"_id": 5, "name": "Radim", "email": "radim@mail.cz"},
    {"_id": 6, "name": "David", "surname": "Novák", "address": "Sázavská 13, Brno"},
    {"_id": 7, "name": "Radka", "surname": "Svodová", "address": "Zimní 55, Olomouc"}
]

response = mycol.insert_many(mylist)

print(response.inserted_ids)

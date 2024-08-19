from connect_mongo import *


mycol = mydb["customers"]

myquery = {"surname": "Čermák"}
mycol.delete_one(myquery)

customers = mycol.find({}, {"_id": 0}).sort("surname")
for customer in customers:
    print(customer)

print('-'*80)
myquery = {"surname": "Svoboda"}
mycol.delete_one(myquery)

customers = mycol.find({}, {"_id": 0}).sort("surname")
for customer in customers:
    print(customer)

print('-'*80)
myquery = {"surname": "Novák"}
response = mycol.delete_many(myquery)
print(f"Bylo smazáno {response.deleted_count} záznamů.")

customers = mycol.find({}, {"_id": 0}).sort("surname")
for customer in customers:
    print(customer)

print('-'*80)
response = mycol.delete_many({})
print(f"Bylo smazáno {response.deleted_count} záznamů.")

from connect_mongo import *


mycol = mydb["customers"]

myquery = {"surname": "Svoboda"}
customer = mycol.find_one(myquery)
print(customer)

# update one
new_values = {"$set": {"address": "Podzimní 6, Ostrava"}}
mycol.update_one(myquery, new_values)
customer = mycol.find_one(myquery)
print(customer)

# update many
print('-'*80)
myquery = {"address": {"$regex": "Brno$"}}
customers = mycol.find(myquery)
for customer in customers:
    print(customer)
new_values = {"$set": {"district": "Jihomoravský kraj"}}
response = mycol.update_many(myquery, new_values)
print(f"Bylo změněno {response.modified_count} záznamů.")

print('-'*40)
customers = mycol.find(myquery)
for customer in customers:
    print(customer)

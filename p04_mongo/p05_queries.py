from connect_mongo import *


mycol = mydb["customers"]

myquery = {"surname": "Novák"}
print(f"Result for query {myquery}:")
response = mycol.find(myquery)
for item in response:
    print(item)

print('-'*80)
myquery = {"surname": {"$gt": "N"}}
print(f"Result for query {myquery}:")
response = mycol.find(myquery)
for item in response:
    print(item)

print('-'*80)
#mycol.insert_one({"name": "David", "surname": "Čermák"})
myquery = {"surname": {"$gt": "N"}}
print(f"Result for query {myquery}:")
response = mycol.find(myquery)
for item in response:
    print(item)

print('-'*80)
myquery = {"surname": {"$regex": "^N"}}
print(f"Result for query {myquery}:")
response = mycol.find(myquery)
for item in response:
    print(item)

print('-'*80)
myquery = {"address": {"$regex": "Brno$"}}
print(f"Result for query {myquery}:")
response = mycol.find(myquery)
for item in response:
    print(item)

#mycol.insert_one({"name": "David", "surname": "Novák"})
print('-'*80)
myquery = {"surname": "Novák"}
print(f"Result for query {myquery}:")
response = mycol.find(myquery)
for item in response:
    print(item)

print("-"*80)
myquery = {"surname": "Novák", "name": "David"}
print(f"Result for query {myquery}:")
response = mycol.find(myquery, {"_id": 0})
for item in response:
    print(item)
    print(f"Customer: {item["name"]} {item["surname"]}")

print("-"*80)
print("All customers:")
customers = mycol.find({}, {"_id": 0})
for customer in customers:
    print(customer)

print("-"*80)
print("All customers - sorted by surname ascending")
customers = mycol.find({}, {"_id": 0}).sort("surname")
for customer in customers:
    print(customer)

print("-"*80)
print("All customers - sorted by surname descending")
customers = mycol.find({}, {"_id": 0}).sort("surname", -1)
for customer in customers:
    print(customer)

print("-"*80)
print("All customers - sorted by surname and name")
myquery = {"surname": {"$exists": "true"}, "name": {"$exists": "true"}}
customers = mycol.find(myquery, {"_id": 0}).sort("name").sort("surname")
for customer in customers:
    print(customer)

print("-"*80)
print("All customers without surname")
myquery = {"surname": {"$not": {"$exists": "true"}}}
customers = mycol.find(myquery, {"_id": 0}).sort("name").sort("surname")
for customer in customers:
    print(customer)

print("-"*80)
print("First 3 customers")
customers = mycol.find().sort("surname").limit(3)
for customer in customers:
    print(customer)

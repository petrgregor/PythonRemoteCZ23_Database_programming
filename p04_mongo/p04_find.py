from connect_mongo import *

mycol = mydb["customers"]

# find_one - vratí první vyhovující záznam
print("Find one:")
response = mycol.find_one()

print(response)

print("Find:")
for response in mycol.find():
    print(response)

print("Find (selected attributes):")
for response in mycol.find({}, {"_id": 0, "name": 1, "surname": 1}):
    print(response)

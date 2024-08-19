import json

from connect_mongo import *

# Use data in medical-data.json to create a new collection: medicaldata
mycol = mydb["medicaldata"]

"""
with open('medical-data.json') as f:
    data = json.load(f)

    response = mycol.insert_many(data)

    print(f"To database 'medicaldata' were inserted {len(response.inserted_ids)} documents.")
"""

# Find all rows with procedure_code equal 0F1F4ZC
print("Find all rows with procedure_code equal 0F1F4ZC")
query = {'procedure_code': "0F1F4ZC"}
procedures = mycol.find(query)
for procedure in procedures:
    print(procedure)

print('-'*80)
# Find patient with patient_id equal 74, print his full name
print("Find patient with patient_id equal 74, print his full name")
query = {'patient_id': 74}
patient = mycol.find_one(query)
print(f"{patient["first_name"]} {patient["last_name"]}")

print('-'*80)
# Find a procedure performed on 2019-05-24T01:52:37.000Z and update its procedure code to 0F1F4ZC
print("Find a procedure performed on 2019-05-24T01:52:37.000Z and update its procedure code to 0F1F4ZC")
query = {"visit_date.date": "2019-05-24T01:52:37.000Z"}
visits = mycol.find(query)
for visit in visits:
    print(visit)
new_values = {"$set": {"procedure_code": "0F1F4ZC"}}
response = mycol.update_many(query, new_values)
print(f"Number of updated documents: {response.modified_count}.")
visits = mycol.find(query)
for visit in visits:
    print(visit)

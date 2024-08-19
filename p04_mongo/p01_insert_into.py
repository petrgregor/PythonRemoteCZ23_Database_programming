from connect_mongo import *


mycol = mydb["test_collection"]

response = mycol.insert_one({"test": "data", "number": 3})

print(response.inserted_id)

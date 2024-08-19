import pymongo
from pymongo import MongoClient


# vytvoříme klienta
#myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")
myclient = pymongo.MongoClient("127.0.0.1", 27017)

# vytvoření databáze
#mydb = myclient.test_db
mydb = myclient["PythonRemoteCZ23"]

if __name__ == '__main__':
    print(f"myclient: {myclient}")
    print(f"mydb: {mydb}")

    databases = myclient.list_database_names()
    print(databases)

    # vytvoření kolekce
    mycol = mydb["customers"]

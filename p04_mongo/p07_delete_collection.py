from connect_mongo import *


mycol = mydb["customers"]

# smazání kolekce
mycol.drop()

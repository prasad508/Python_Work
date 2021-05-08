# MangoDB practical

import pymongo


mc =    pymongo.MongoClient("mongodb://localhost:27017/testdb")
mydb = mc["testdb"]

print(mc.list_database_names())

dblist = mc.list_database_names()
if "mydb" in dblist:
    print("Database is exit")

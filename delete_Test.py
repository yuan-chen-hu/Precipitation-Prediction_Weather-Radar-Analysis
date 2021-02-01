import pymongo
import json
from collections import namedtuple
from bson import ObjectId

# ----------------connect mongodb------------------
myclient = pymongo.MongoClient("mongodb")


# ----------------create/connect database------------------
mydb = myclient["mydatabase"]

# ----------------create/connect collections------------------
mycol = mydb["customers"]

# ----------------check if database exist------------------
dblist = myclient.list_database_names()
if "mydatabase" in dblist:
  print("connect to database.")

# ----------------check if collecgtion exist------------------
collist = mydb.list_collection_names()
if "customers" in collist:
  print("connect to collection.")

# import time
# print(time.strftime("%Y%m%d%H%M"))

# ----------------insert------------------
# mydict = { "_id": 1, "name": "John", "address": "Highway 37" }
# x = mycol.insert_one(mydict)
# mydict = { "_id": 2, "name": "steven", "address": "Taipei" }
# x = mycol.insert_one(mydict)

# # ----------------delete------------------
# myquery = { "address": "Taipei" }
# mycol.delete_one(myquery)
# -------------------delete one

#for x in mycol.find().limit(1):
#	mycol.delete_one(x)

# ----------------delete all------------------
#for x in mycol.find():
#  mycol.delete_one(x)

# ----------------find all data in collection and print------------------
count=0 
for x in mycol.find():
	print(count)
	count+=1
#   print(x)
#-----------------------limit 5 and delete exceed data---------------
print("limit 5 and delete exceed data")
data_on_web_count=0
while data_on_web_count>5:
	for last_one in mycol.find():
		data_on_web_count+=1
		print("data_on_web_count=",data_on_web_count)
	print("final data_on_web_count=",data_on_web_count)	
	for last_one in mycol.find().limit(1):
		mycol.delete_one(last_one)	

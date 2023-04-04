import pymongo
client = pymongo.MongoClient("mongodb+srv://nishanthssv:PleaseRemember123@clustern.gn40smy.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d = {
    "name" : "nishanth",
    "email" : "abc@dbc.com",
    "surname" : "shylendra"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
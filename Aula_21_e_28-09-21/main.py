import pymongo

client = pymongo.MongoClient("mongodb+srv://ghelfer:chimarrao@iotdb.asglx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.IoTdb
collection = db.Sensores
x = collection.find().sort("pressao")
for i in x:
    print(i['_id'])
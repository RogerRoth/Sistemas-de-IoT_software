import pymongo

client = pymongo.MongoClient("mongodb+srv://nosql10440610:<password>@cluster0.w02qr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.IoTdb
collection = db.Sensores
x = collection.find().sort("pressao")
for i in x:
    print(i['_id'])
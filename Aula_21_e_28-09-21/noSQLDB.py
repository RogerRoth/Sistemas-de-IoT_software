# arquivo de funções e conexões do banco de dados não relacional relacional
import pymongo

'''
Host: cloud.mongodb.com/
Database name: sql10440610
Database user: nosql10440610
Database password: 9vVIK9d3qA
'''

client = pymongo.MongoClient("mongodb+srv://nosql10440610:9vVIK9d3qA@cluster0.w02qr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.IoTdb
collection = db.Pessoa
result = collection.find()


def insertRegister(array):
    val = {f"nome":array[1], "idade":array[2], "altura":array[3], "pais":array[4]}
    x = collection.insert_one(val)


def buscaTodosRegistros():
    result = collection.find()
    aux = []
    for i in result:
        aux.append(i)
    return aux


insertRegister((1, 'Carlos Alberto', '40', '1.70', 'Brasil'))

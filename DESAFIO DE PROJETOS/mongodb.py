import datetime
from pprint import pprint
import pymongo as pyM

customer = pyM.MongoCustomer("mongodb+srv://@pymongo.tz2mj8a.mongodb.net/?retryWrites=true&w=majority")

db = customer.test
collection = db.test_collection
print(db.test_collection)

transacao = {
    "User": "Lorrany",
    "cpf" :"11254654600",
    "date": datetime.datatime.utcnow()
}

transacao = db.transacao
transacao_id = transacao.insert_one(transacao).insert_id
print(db.transacao)

pprint.pprint(db.transacao.find_one())
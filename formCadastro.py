import pymongo
from bson.json_util import dumps


dburi = "mongodb+srv://appbasicuser:appbasicusert3st3@cluster0-jvnpg.mongodb.net/test?retryWrites=true"
dbname = "test"
dbcollectionname = "messages"
	
def saveCadastro(item):
	client = pymongo.MongoClient(dburi)
	db = client[dbname]
	dbcollection = db[dbcollectionname]
	itemid = dbcollection.insert_one(item).inserted_id
	return str(itemid)


def listCadastro():	
	client = pymongo.MongoClient(dburi)
	db = client[dbname]	
	dbcollection = db[dbcollectionname]	
	cursor = dbcollection.find().sort("timestamp", -1).limit(10) 
	return dumps(cursor)
	
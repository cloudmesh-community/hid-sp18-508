from pymongo import MongoClient
# Connect to the MongoDB, change the connection string per your MongoDB environment
client = MongoClient(port=27017)
# Set the db object to point to the business database
db=client.variables
# Showcasing the count() method of find, count the total number of 5 ratings

def get_profile():
	l = list()
	for each in db.Var.find():
		l.append((each['uuid'], each['username'], each['context'],each['description'],each['firstname'],each['lastname'],each['publickey'],each['email']))
	return l

def get_profile_by_uuid_mongo(uuid):
	for each in db.Var.find({'uuid':uuid}):
		return (each['uuid'], each['username'], each['context'],each['description'],each['firstname'],each['lastname'],each['publickey'],each['email'])

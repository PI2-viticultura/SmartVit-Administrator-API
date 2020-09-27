from flask_pymongo import PyMongo, MongoClient

client = MongoClient('mongodb://admin-mongodb:27017/', username='admin', password='password')
db = client.smartDevApiService
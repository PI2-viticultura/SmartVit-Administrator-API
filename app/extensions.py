from flask_pymongo import MongoClient
import os

password = os.environ["MONGOPASSWORD"]
dbname = os.environ["DBNAME"]
env = os.environ["ENVIRONMENT"]

client = MongoClient(
    "mongodb+srv://smartAdmin:"
    + password + "@smartvit.6s6r9.mongodb.net/"
    + dbname + "?retryWrites=true&w=majority"
)

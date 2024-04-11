from pymongo import MongoClient, errors
from bson.json_util import dumps
import os


MONGOPASS = os.getenv('MONGOPASS') #populating variable from environment variable
uri = "mongodb+srv://cluster0.pnxzwgz.mongodb.net/sample_restaurants" #url to server itself - my endpoint in atlas
client = MongoClient(uri, username='nmagee', password=MONGOPASS, connectTimeoutMS=200, retryWrites=True) #creating a client
sampler = client.sample_restaurants # sample client restaurant database
restaurants = sampler.restaurants # database and restaurant collection
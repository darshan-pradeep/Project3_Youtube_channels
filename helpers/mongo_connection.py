import pymongo
import os

def mongo_connector():
    password=os.environ['MONGODB_PASSWORD']
    link="mongodb+srv://mongodb:{a}@cluster0.zg3uh.mongodb.net/?retryWrites=true&w=majority".format(a=password)
    client = pymongo.MongoClient(link)
    db = client.test
    print('connection established with Mongodb')
    return client
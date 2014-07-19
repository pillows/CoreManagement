import hashlib
import pymongo

db = pymongo.MongoClient("localhost", 27017).coremanagement

def protect(string):
    seed = database.getSeed()
    for x in range(1000):
        for x in range(100):
            string = hashlib.sha256(string).hexdigest()
        string = hashlib.sha512(string).hexdigest()

    return string

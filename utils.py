import hashlib
import pymongo

db = pymongo.MongoClient("localhost", 27017).coremanagement

def protect(string):
    seed = "ASDkk;12lk3kl1;23kl;;alsdkdslfk;dskjfjksDFKJjkljklJKjklJJjkKLJskajdjkjk34239i493i29((#()@01023102939)()(@09133920"
    for x in range(1000):
        for x in range(100):
            string = hashlib.sha256(string).hexdigest()
        string = hashlib.sha512(string).hexdigest()

    return string

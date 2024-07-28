from pymongo import MongoClient
from datetime import datetime
client = MongoClient('localhost', 27017)
# wtaMasterList2024-01-07/27/24

db = client.tennisdb

test = db.test
tennis = db.tennis 

# test.insert_one({'name': 'Testboy Mr Dungbeetle'})
# for person in test.find():
#     print(person)

def send_to_db(key, content='test'):
    name = key + datetime.today().strftime('%Y-%m-%d') 
    tennis.insert_one({'name':name, 'content':content})

def get_from_db(key): 
    return [t for t in tennis.find({"name" : key} )]

#print(get_from_db('wtaMasterList2024-07-28'))

# for list in tennis.find():
#     print(list)

# print(datetime.today().strftime('%Y-%m-%d')) 
# print([i for i in tennis.find({'name' : 'wtaMasterList2024-01-07/27/24'})])
from pymongo import MongoClient
from datetime import datetime
from io import  BytesIO
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

'''
The basic databank setup
'''

client = MongoClient('mongo', 27017)
db = client.tennisdb
test = db.test 
tennis = db.tennis 

'''
The databank calls
'''

def send_to_db(key, content='test'):
    name = key + datetime.today().strftime('%Y-%m-%d') 
    tennis.insert_one({'name':name, 'content':content})

def get_from_db(key): 
    #return [t for t in tennis.find({"name" : key} )]
    name = key + datetime.today().strftime('%Y-%m-%d')
    return tennis.find_one({'name':name})

def send_graph_to_db(key):
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_binary = buffer.getvalue()
    buffer.close()
    document = {
        'name' : key + datetime.today().strftime('%Y-%m-%d'), 
        'img' : image_binary
    }
    tennis.insert_one(document)

def return_graph(key):
    #name = key + datetime.today().strftime('%Y-%m-%d')
    document = tennis.find_one({'name' : key})
    if document is None:
        return print('no doc found')
    else:
        print(document)
        image_binary = document['img']
        buffer = BytesIO(image_binary)
        buffer.seek(0)
        img = mpimg.imread(buffer, format='png')
        buffer.close()
        plt.imshow(img)
        plt.show()

def get_client():
    return db

def show_names():
    for document in tennis.find({}, {'_id':0, 'name':1}):
        print(document.get('name'))

def get_old_from_db(title, date):
    name = title + date
    return tennis.find_one({'name':name})

'''
Some useful test print statements for testing database connectivity
'''
# return_graph('top20_wta500_countries_ranked_by_appearance2024-07-28')
# test.insert_one({'name': 'Testboy Mr Dungbeetle'})
# for person in test.find():
#     print(person)

#print(get_from_db('wtaMasterList2024-07-28'))

# for list in tennis.find():
#     print(list)

# print(datetime.today().strftime('%Y-%m-%d')) 
# print([i for i in tennis.find({'name' : 'wtaMasterList2024-01-07/27/24'})])


#show_names()
#print(get_old_from_db('20150515144023', '2024-08-06'))
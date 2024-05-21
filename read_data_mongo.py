#imports 
from pymongo import MongoClient
from mongo.mongo_helper import check_mongo_status, create_mongo_client
import subprocess



#make the mongo client 
mongo_client = create_mongo_client()


def get_article_data(db_name,collection_name,article_name):
    """
    Find the specific data from the collection
    """

    db = mongo_client[db_name]
    collection = db[collection_name]

    if collection is not None:
        # Retrieve all documents in the collection
        page_data = collection.find_one(article_name)
    
    return page_data


#for test testing the data 

#data = show_article_data(db_name,collections[0],{'article_name': 'patching-unpatching'})

#print(data)
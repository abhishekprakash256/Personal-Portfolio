
import redis
import os

"""
redis_host = os.getenv('REDIS_HOST', 'localhost')  # Use 'localhost' or the Docker host IP
redis_port = int(os.getenv('REDIS_PORT', 6379))

redis_client = redis.Redis(host=redis_host, port=redis_port)


print(redis_client)


from pymongo import MongoClient
import os

mongo_host = os.getenv('MONGO_HOST', 'localhost')  # Use 'localhost' or the Docker host IP
mongo_port = int(os.getenv('MONGO_PORT', 27017))


mongo_client = MongoClient(mongo_host, mongo_port)

try:
    # Create a MongoDB client
    client = MongoClient(mongo_host, mongo_port)
    print("MongoDB client created successfully.")
except Exception as e:
    print(f"Error creating MongoDB client: {e}")
    


db = mongo_client["test"]


print(db)
"""


#from mongo.mongo_helper import check_mongo_status, create_mongo_client


#make the mongo client 
#mongo_client = create_mongo_client()

#print(mongo_client)

from pymongo import MongoClient
import os
import redis

def get_mongo_client():
    mongo_host = os.getenv('MONGO_HOST', 'localhost')
    mongo_port = int(os.getenv('MONGO_PORT', 27017))

    try:
        client = MongoClient(mongo_host, mongo_port)
        print("MongoDB client created successfully.")
        return client
    except Exception as e:
        print(f"Error creating MongoDB client: {e}")
        return None

def get_redis_client():
    redis_host = os.getenv('REDIS_HOST', 'localhost')
    redis_port = int(os.getenv('REDIS_PORT', 6379))

    try:
        client = redis.Redis(host=redis_host, port=redis_port)
        print("Redis client created successfully.")
        return client
    except Exception as e:
        print(f"Error creating Redis client: {e}")
        return None

def insert_test_data(client):
    try:
        db = client['testdb']
        collection = db['testcollection']
        test_data = {'name': 'test', 'value': 123}
        result = collection.insert_one(test_data)
        print(f"Data inserted with ID: {result.inserted_id}")
    except Exception as e:
        print(f"Error inserting data: {e}")

if __name__ == '__main__':
    mongo_client = get_mongo_client()
    if mongo_client:
        insert_test_data(mongo_client)

    redis_client = get_redis_client()
    if redis_client:
        redis_client.set('testkey', 'testvalue')
        print(f"Redis set testkey: {redis_client.get('testkey').decode('utf-8')}")


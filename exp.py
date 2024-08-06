
import redis
import os


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
    



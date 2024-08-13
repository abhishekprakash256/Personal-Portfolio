"""
make the dummy flask app
"""
from pymongo import MongoClient
import redis
from flask import Flask

app = Flask(__name__)

def mongo_connection():
    try:
        # Connect to MongoDB using the container name
        #client = MongoClient('localhost', 27017, serverSelectionTimeoutMS=2000)  # 2-second timeout
        client = MongoClient('mongo', 27017, serverSelectionTimeoutMS=2000)  # 2-second timeout
        client.server_info()  # This forces a connection attempt.
        print("MongoDB client created successfully.")
    except Exception as e:
        print("MongoDB client not working:", e)


def redis_client():
    try:
        # Connect to Redis using the container name
        #client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
        client = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)
        client.ping()  # Pinging the server to ensure it's up.
        print("Redis client created successfully.")
    except Exception as e:
        print("Redis client is not working:", e)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    mongo_connection()
    redis_client()
    app.run(host='0.0.0.0', port=5000, debug=True)




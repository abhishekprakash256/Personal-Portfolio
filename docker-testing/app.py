"""
make the dummy flask app
"""
from pymongo import MongoClient
import redis
from flask import Flask
import subprocess
import os



app = Flask(__name__)


"""
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

"""
def check_mongo_status():
    try:
        # Execute the command to check MongoDB server status
        result = subprocess.run(['mongod', '--version'], capture_output=True, text=True)
        
        # Check if the command was successful
        if result.returncode == 0:
            print("MongoDB is installed")
            return True
        else:
            print("MongoDB is not installed or not running.")
            return False
    
    except FileNotFoundError:
        # Handle the case where 'mongod' command is not found (MongoDB not installed)
        print("MongoDB is not installed.")
        return False

def create_mongo_client():


    mongo_status = check_mongo_status()

    if mongo_status:
        try:

            #new code ----
            #mongo_host = os.getenv('MONGO_HOST', 'localhost')  # Use 'localhost' or the Docker host IP
            #mongo_port = int(os.getenv('MONGO_PORT', 27017))
            #client = MongoClient(mongo_host, mongo_port)


            # Attempt to create a MongoClient -- old code
            client = MongoClient('mongo', 27017, serverSelectionTimeoutMS=2000)  # 2-second timeout  # new code
            #client = MongoClient('localhost', 27017)
            client.server_info()  # This forces a connection attempt.
            print("MongoDB client created successfully.")
            #print("client is created")
            return client

        except ImportError:
            # Print error message if pymongo is not installed
            print("MongoDB is not installed on this system.")
            return None

        except Exception as e:
            # Print error message if MongoClient creation fails for other reasons
            print("Error creating MongoDB client:", e)
            return None
    
    else:
        return "Mongo Missing"


def check_redis_status():
    try:
        # Execute the command to check MongoDB server status
        result = os.system("redis-cli 'ping'")
        
        # Check if the command was successful
        if result == 0:
            print("Redis is installed and running.")
            return True
        else:
            print("Redis is not installed or not running.")
            return False
    
    except FileNotFoundError:
        # Handle the case where 'mongod' command is not found (MongoDB not installed)
        print("Redis is not installed.")
        return False



#create the database client 
def create_redis_client():


    redis_status = check_redis_status()

    if redis_status:
        try:

            #new code ---
            #redis_host = os.getenv('REDIS_HOST', 'localhost',port=6379, db=0, decode_responses=True)  # Use 'localhost' or the Docker host IP
            #redis_port = int(os.getenv('REDIS_PORT', 6379))
            #client = redis.Redis(host=redis_host, port=redis_port)

            # Attempt to create a Redis client
            client = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)   #new code
            #client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
            client.ping()  # Pinging the server to ensure it's up.
            print("Redis client created successfully.")
            return client

        except ImportError:
            # Print error message if pymongo is not installed
            print("Redis is not installed on this system.")
            return None

        except Exception as e:
            # Print error message if MongoClient creation fails for other reasons
            print("Error creating Redis client:", e)
            return None
    
    else:
        return "Redis Missing"




@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    create_mongo_client()
    create_redis_client()
    app.run(host='0.0.0.0', port=5000, debug=True)




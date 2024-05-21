"""
The redis helper function to add the connection and methods to add the data 
"""

#imports 
import redis
import os 


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

            # Attempt to create a MongoClient
            client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
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



redis_client = create_redis_client()

class Helper_fun():

    def __init__(self, hash_name, set_name):
        self.hash_name = hash_name
        self.set_name = set_name

    def add_value_to_set(self,value):
        """
        The function to add value to the set 
        """
        #add the value to the set 

        res = redis_client.sadd(self.set_name, value)

        if res: 
            print("Data added in set succesfully")
        
        else:
            print("Failed to add data in set")
    
    
    def add_value_to_hash(self, key , value):
        """
        The function to add value to the set 
        """
        #add the value to the set 

        res = redis_client.hset(self.hash_name, key, value)

        #testting the code
        #print(type(key))
        #print(type(value))

        #print(res)

        if res: 
            print("Data added in hash succesfully")
        
        else:
            print("Failed to add data in hash")

    
    def delete_db(self,db_name):
        """
        The function to delete the hash if exists 
        and then delete the hash
        """
        # check the hash exists 
        if redis_client.exists(db_name):
            
            #delete the hash or set 
            redis_client.delete(db_name)
            print("The db has been deleted succesfully")
        
        else:

            print("The db doesn't exists")

    
    def pop_set_val(self):
        """
        The funcion to pop a value from the set 
        """

        res = redis_client.spop(self.set_name)

        if res:
            return res
        
        else:
            return None
    
    def get_hash_value(self,hash_val):
        """
        The function to get the hash value 
        """
        res = redis_client.hget(self.hash_name, hash_val)
        if res:
            return res
        else:
            return "Value not found"

    def check_hash_exist(self,hash_val):
        """
        The function to check the hash value exist in the set and in the redis hash
        """

        hash_check = redis_client.hexists(self.hash_name, hash_val)
        
        if hash_check:
            return True 
        
        else:
            return False
    
    def get_all_set_val(self):
        """
        The function to get all the hash value 
        """

        set_members = redis_client.smembers(self.set_name)
        
        print("Values in Redis set :")
        
        for member in set_members:
            print(member)
            

    def get_all_hash_val(self):
        """
        The function to get all the set value 
        """

        hash_fields = redis_client.hgetall(self.hash_name)
        print("\nFields and values in Redis hash ")
        for field, value in hash_fields.items():
            print(f"{field}: {value}")

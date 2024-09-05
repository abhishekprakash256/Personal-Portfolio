#imports 
from pymongo import MongoClient
import subprocess
from datetime import datetime
import traceback
import os


#const values
collection_lst = ["projects","tech","life"]


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


#create the database client 
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

"""
#new code
def create_mongo_client():
    hosts = ['localhost', 'mongo']  # List of hosts to try
    for host in hosts:
        try:
            # Try connecting to MongoDB using the current host
            client = MongoClient(host, 27017, serverSelectionTimeoutMS=2000)  # 2-second timeout
            client.server_info()  # This forces a connection attempt.
            print(f"MongoDB client created successfully using host: {host}")
            return client
        except Exception as e:
            print(f"Failed to connect to MongoDB using host {host}: {e}")
    
    # If neither host works, raise an exception or return None
    print("Failed to create MongoDB client with all host options.")
    return None






#make the mongo client 
mongo_client_docker = create_mongo_client()



#the helper class for the mongo functions 
# Helper class for MongoDB functions
class Helper_fun():

    def __init__(self,client = mongo_client_docker):
        self.mongo_client = client

    def make_database_and_collection(self, db_name, db_collection):
        """
        Make the database and collection if they don't exist
        """
        # Print the list of existing databases before attempting to create the database
        print("Existing databases before creating '{}':".format(db_name), self.mongo_client.list_database_names())

        # Make the database if it doesn't exist
        if db_name not in self.mongo_client.list_database_names():
            # Create the database
            db = self.mongo_client[db_name]

            # Create the collection
            collection = db[db_collection]

            # Insert dummy data into the collection
            dummy_data = {"dummy_data": True}
            insert_data = collection.insert_one(dummy_data)

            print("Database '{}' and collection '{}' created.".format(db_name, db_collection))
        else:
            # If the database exists, select it
            db = self.mongo_client[db_name]
            collection = db[db_collection]
            print("Database '{}' already exist.".format(db_name, db_collection))
        
        # Print the list of existing databases after attempting to create the database
        print("Existing databases after creating '{}':".format(db_name), self.mongo_client.list_database_names())

    def make_collections(self,db_name,collection_name):
        """
        The function to make the collection in the database
        """
        db = self.mongo_client[db_name]


        if collection_name not in db.list_collection_names():
            db.create_collection(collection_name)
            print("Collection '{}' created.".format(collection_name))

        else:
            print("Collection '{}' already exists.".format(collection_name))



    def show_collections(self,db_name):
        """
        show the collections
        """
        db = self.mongo_client[db_name]

        collections = db.list_collection_names()

        for collection_lst in collections:
            print(collection_lst)



    def show_all_data(self,db_name,collection_name):
        """
        Show the data in the collection
        """
        db = self.mongo_client[db_name]
        collection = db[collection_name]


        if collection is not None:
            # Retrieve all documents in the collection
            documents = collection.find()

            # Print each document
            for document in documents:
                print(document)
        else:
            print("No collection available. Please create a collection first.")
        
    def show_article_data(self,db_name,collection_name,article_name):
        """
        Find the specific data from the collection
        """

        db = self.mongo_client[db_name]
        collection = db[collection_name]

        if collection is not None:
            # Retrieve all documents in the collection
            page_data = collection.find_one(article_name)
        
        return page_data



    def insert_data(self,db_name,collection_name,data):
        """
        Insert the data into the database and collection
        """
        db = self.mongo_client[db_name]
        collection = db[collection_name]

        #if the data is None 
        if data is None:
            return "data is Null"
        

        # Check if any documents match the criteria
        existing_data = collection.find_one(data)

        if existing_data is None:
        
        #insert the data
            
            for page_data in data:
                insert_data_res = collection.insert_one(page_data)

        #condtion to check for the data is inserted 
            if insert_data_res.acknowledged :
                print("Data inserted succesfuly")
    
            else:
                print("Data not inserted")
        
        else:
            print("Data  already exist")


    def delete_data(self,db_name,collection_name,data):
        """
        The function to delete the data
        """
        #if the data is None 
        if data is None:
            return "data is Null"
        
        db = self.mongo_client[db_name]
        collection = db[collection_name]

        # Check if any documents match the criteria
        existing_data = collection.find_one(data)

        # Delete a single document that matches the criteria
        delete_result = collection.delete_one(data)

        if delete_result.deleted_count == 1:
            print("Data deleted successfully.")
        else:
            print("No record matched the data")

    def modify_data_one(self,db_name,collection_name,filter_criteria,new_data):
        """
        The function to modify the data in mongodb as per collection and db
        """

        #if the data is None 
        if new_data is None:
            return "data is Null"
    
        db = self.mongo_client[db_name]
        collection = db[collection_name]
    
        #update the data in collection
        if collection.update_one(filter_criteria,new_data):  # Update the data 
            print("Update succesfull")
        
        else:
            print("Update failed")

    def delete_db(self,db_name):
        """
        The function to delete the database
        """
        db = self.mongo_client[db_name]
        
        #drop the database
        self.mongo_client.drop_database(db_name)

        print("The database has been deleted")
    

    def delete_data_all(self,db_name,collection_name):
        """
        The funciton to delete all the data inside a collection
        """
        pass



    # the chat app data fetching methods  --- 

    def insert_message_data(self,db_name,collection_name,chat_hash,sender_hash, recipient_hash, message):
        """
        The funciton to insert the message in the database and collection
        """
        db = self.mongo_client[db_name]
        collection = db[collection_name]

        message_doc = {
        'chat_hash': chat_hash,
        'sender_hash': sender_hash,
        'recipient_hash': recipient_hash,
        'message': message,
        'timestamp': datetime.now()
        }

        if collection.insert_one(message_doc):
            print("Succesfull insertion")
        else:
            print("failed to insert message")
    
    def get_chat_messages(self,db_name,collection_name,chat_hash):
        """
        The function to get the messages from the database
        """

        db = self.mongo_client[db_name]
        collection = db[collection_name]


        return collection.find({'chat_hash': chat_hash}).sort('timestamp', 1)

    def delete_message(self, db_name, collection_name, chat_hash):
        """
        The function to delete messages based on chat_hash
        """
        db = self.mongo_client[db_name]
        collection = db[collection_name]

        try:
            # delete the data
            delete_result = collection.delete_many({'chat_hash': chat_hash})

            if delete_result.deleted_count > 0:
                print("Chat data erased")
            else:
                print("No records found to delete")
        except Exception as e:
            print(f"Error deleting message: {e}")
            traceback.print_exc()
    


    

        





    
        


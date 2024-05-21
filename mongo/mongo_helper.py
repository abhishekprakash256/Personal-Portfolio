#imports 
from pymongo import MongoClient
import subprocess


#const values
collection_lst = ["projects","tech","life"]



def check_mongo_status():
    try:
        # Execute the command to check MongoDB server status
        result = subprocess.run(['mongod', '--version'], capture_output=True, text=True)
        
        # Check if the command was successful
        if result.returncode == 0:
            print("MongoDB is installed and running.")
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

            # Attempt to create a MongoClient
            client = MongoClient('localhost', 27017)
            print("MongoDB client created successfully.")
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


#make the mongo client 
mongo_client = create_mongo_client()



#the helper class for the mongo functions 
# Helper class for MongoDB functions
class Helper_fun():

    def make_database_and_collection(self, db_name, db_collection):
        """
        Make the database and collection if they don't exist
        """
        # Print the list of existing databases before attempting to create the database
        print("Existing databases before creating '{}':".format(db_name), mongo_client.list_database_names())

        # Make the database if it doesn't exist
        if db_name not in mongo_client.list_database_names():
            # Create the database
            db = mongo_client[db_name]

            # Create the collection
            collection = db[db_collection]

            # Insert dummy data into the collection
            dummy_data = {"dummy_data": True}
            insert_data = collection.insert_one(dummy_data)

            print("Database '{}' and collection '{}' created.".format(db_name, db_collection))
        else:
            # If the database exists, select it
            db = mongo_client[db_name]
            collection = db[db_collection]
            print("Database '{}' already exist.".format(db_name, db_collection))
        
        # Print the list of existing databases after attempting to create the database
        print("Existing databases after creating '{}':".format(db_name), mongo_client.list_database_names())

    def make_collections(self,db_name,collection_name):
        """
        The function to make the collection in the database
        """
        db = mongo_client[db_name]


        if collection_name not in db.list_collection_names():
            db.create_collection(collection_name)
            print("Collection '{}' created.".format(collection_name))

        else:
            print("Collection '{}' already exists.".format(collection_name))



    def show_collections(self,db_name):
        """
        show the collections
        """
        db = mongo_client[db_name]

        collections = db.list_collection_names()

        for collection_lst in collections:
            print(collection_lst)



    def show_all_data(self,db_name,collection_name):
        """
        Show the data in the collection
        """
        db = mongo_client[db_name]
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

        db = mongo_client[db_name]
        collection = db[collection_name]

        if collection is not None:
            # Retrieve all documents in the collection
            page_data = collection.find_one(article_name)
        
        return page_data



    def insert_data(self,db_name,collection_name,data):
        """
        Insert the data into the database and collection
        """
        db = mongo_client[db_name]
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
        
        db = mongo_client[db_name]
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
    
        db = mongo_client[db_name]
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
        db = mongo_client[db_name]
        
        #drop the database
        mongo_client.drop_database(db_name)

        print("The database has been deleted")

    def delete_data_all(self,db_name,collection_name):
        """
        The funciton to delete all the data inside a collection
        """
        pass


    


    

        





    
        


"""
The file has the calling of the methods to 
"""


#imports 
#the helper funciton to help the mongo db data insertion 
from mongo_helper import Helper_fun, create_mongo_client

#the read data from the json files
from read_data_json import *
from pymongo import MongoClient


#const files
#articles file path 
PROJECT_ARTICLE_FILE_PATH = "../static/project_article_data.json"
TECH_ARTICLE_FILE_PATH = "../static/tech_article_data.json"

#section file path
SECTION_FILE_PATH = "../static/section_data.json"


ARTICLE_FILE_PATH_LST = [PROJECT_ARTICLE_FILE_PATH,TECH_ARTICLE_FILE_PATH]
SECTION_FILE_PATH_LST = [SECTION_FILE_PATH]


#db names in mongo
db_name = ["articles","section"]


#collection names in database 
collections_article = ["projects","tech"] #life 
collection_section = ["section_data"]



def create_alternative_mongo_client():
    try:
        # Connect to MongoDB using localhost instead of Docker's internal network
        client = MongoClient('localhost', 27017, serverSelectionTimeoutMS=2000)  # 2-second timeout
        #client = MongoClient('mongo', 27017, serverSelectionTimeoutMS=2000)  # 2-second timeout
        client.server_info()  # This forces a connection attempt.
        print("Alternative MongoDB client created successfully.")
        return client
    except Exception as e:
        print("Alternative MongoDB client not working:", e)
        return None

# Step 2: Override the `mongo_client` variable using the new function
mongo_client = create_alternative_mongo_client()


if __name__ == "__main__":
    #read the data from the json file 
    helper = Helper_fun(mongo_client)

    #delete the database 
    for db_val in db_name:
        helper.delete_db(db_val)

    
    #start the datbase data insertion 
    
    #start the first loop
    for first_iter in range(1):

        for second_iter in range(2):

            #making the datbase and collections 
            helper.make_database_and_collection(db_name[first_iter], collections_article[second_iter])

            #read the data 
            page_data_list = read_page_data_from_json(file_path = ARTICLE_FILE_PATH_LST[second_iter])

            #delete the dummy data
            helper.delete_data(db_name[first_iter],collections_article[second_iter],{'dummy_data': True})

            #insert the data 
            helper.insert_data(db_name[first_iter],collections_article[second_iter],page_data_list)

            #show the data 
            helper.show_all_data(db_name[first_iter],collections_article[second_iter])
    
    
    #start the second loop 
    for first_iter in range(1,2):

        for second_iter in range(1):

            #making the datbase and collections 
            helper.make_database_and_collection(db_name[first_iter], collection_section[second_iter])

            #read the data 
            page_data_list = read_page_data_from_json(file_path = SECTION_FILE_PATH_LST[second_iter])

            #delete the dummy data
            helper.delete_data(db_name[first_iter],collection_section[second_iter],{'dummy_data': True})

            #insert the data 
            helper.insert_data(db_name[first_iter],collection_section[second_iter],page_data_list)

            #show the data 
            helper.show_all_data(db_name[first_iter],collection_section[second_iter])
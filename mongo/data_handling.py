"""
The file has the calling of the methods to 
"""


#imports 
#the helper funciton to help the mongo db data insertion 
from mongo_helper import * 

#the read data from the json files
from read_data_json import *


#const files
#articles file path 
PROJECT_ARTICLE_FILE_PATH = "../static/project_article_data.json"
TECH_ARTICLE_FILE_PATH = "../static/tech_article_data.json"

#section file path
SECTION_FILE_PATH = "../static/section_data.json"


FILE_PATH_LST = [PROJECT_ARTICLE_FILE_PATH,TECH_ARTICLE_FILE_PATH]



#db names in mongo
db_name = ["articles","section"]

#collection names in database 
collections = ["projects","tech","life","section_data"]




if __name__ == "__main__":
    #read the data from the json file 
    page_data_list = read_page_data_from_json(file_path = SECTION_FILE_PATH )

    # Create an instance of the Helper_fun class
    helper = Helper_fun()

    # Make the database and collection
    helper.make_database_and_collection(db_name[1], collections[3])

    #delete the dummy data from 1st collection
    helper.delete_data(db_name[1],collections[3],{'dummy_data': True})

    #make the collections 
    #helper.make_collections(db_name,collections[1])
    #helper.make_collections(db_name,collections[2])

    #show the collections
    helper.show_collections(db_name[1])

    #insert the data in collection 0 
    helper.insert_data(db_name[1],collections[3],page_data_list)

    #show the data 
    helper.show_all_data(db_name[1],collections[3])
    #article_data = helper.show_article_data(db_name,collections[0],{'article_name': 'patching-unpatching'})

    #modify the data
    #filter_criteria = {"article_name":"another-article"}
    #new_data = {"$set": {"article_name": "test-article"}}
    #helper.modify_data_one(db_name,collections[0],filter_criteria,new_data )




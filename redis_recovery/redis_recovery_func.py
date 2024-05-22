import sys
import os
import json

#make the parnet directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'redis_fun'))
sys.path.insert(0, parent_dir)

#import the redis helper function
from redis_helper import *

#const values
HASH_NAME = "url-hash"
SET_NAME = "url-set"
#file path 
JSON_FILE_PATH = "../static/redis_hash.json"

#make the hash map 
hash_mapper = {}


#make the instance 
helper_fun = Helper_fun(HASH_NAME,SET_NAME)


#store the values to dictionary
helper_fun.store_hash_val(hash_mapper)



def save_dict_to_json_file(dictionary, file_path) :
    """
    Save a dictionary to a JSON file.

    Parameters:
    dictionary (dict): The dictionary to save.
    file_path (str): The path to the file where the dictionary should be saved.
    """
    try:
        with open(file_path, 'w') as json_file:
            json.dump(dictionary, json_file, indent=4)
        print(f"Dictionary saved to {file_path}")
    except Exception as e:
        print(f"An error occurred while saving the dictionary to JSON: {e}")


#save the redish hash to json 
save_dict_to_json_file(hash_mapper, JSON_FILE_PATH)
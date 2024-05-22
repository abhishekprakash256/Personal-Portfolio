"""
The file to push the json file hashes to redis hash 
"""

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

print()

#make the instance 
helper_fun = Helper_fun(HASH_NAME,SET_NAME)

#for testing purpose
#helper_fun.delete_db(HASH_NAME)

def push_hash_from_json_to_redis(file_path, hash_name):
    """
    The function to push the value to redis hash from json file 
    """
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        
        # Print the values of the dictionary
        for key, value in data.items():
            #print(f"{key}: {value}")
            helper_fun.add_value_to_hash(key,value)
        
        #print("Values have been added succesfully")


    except Exception as e:
        print(f"An error occurred while reading the JSON file: {e}")


push_hash_from_json_to_redis(JSON_FILE_PATH,HASH_NAME)
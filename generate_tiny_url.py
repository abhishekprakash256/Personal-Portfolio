"""
The file to make the tiny url and combine all the pieces to work together 
inlcluding the checking of the redis and filling the set to have 10 values reserved for hashes 
"""
from redis_fun.redis_helper import *
from hashing.make_hashes import * 


#const values
HASH_NAME = "url-hash"
SET_NAME = "url-set"

#set the length of the pregenrated hashes 
PRE_GEN_HASH_NUM = 10



helper_fun = Helper_fun(HASH_NAME,SET_NAME)



def check_redis_set():
    """
    The function to check if the redis set has 10 unique values prebaked for hashing
    generate here and check the hash and then add in the set
    """
    len_set = redis_client.scard(SET_NAME)

    while len_set < PRE_GEN_HASH_NUM:
        
        #genrate the new hash
        new_hash = generate_random_hash()

        #check if the not exists then add
        if not helper_fun.check_hash_exist(new_hash):
            helper_fun.add_value_to_set(new_hash)
        
        len_set = redis_client.scard(SET_NAME)




def generate_tiny_url_fun(original_url):
    """
    The function to take the url and assign into the hash value 
    put the new value for the mapping from the flask server 
    """
    
    check_redis_set()
    new_url = helper_fun.pop_set_val()

    #test purpose
    #print(new_url)

    #add the url in the redis with new hash value
    helper_fun.add_value_to_hash(new_url, original_url)

    return new_url



#testing purpose --- as per manual testing the code is working 

#generate_tiny_url_fun("www.google.com")


#helper_fun.delete_db(HASH_NAME)
#helper_fun.delete_db(SET_NAME)
#helper_fun.get_all_hash_val()
#helper_fun.get_all_set_val()
#print(type(helper_fun.get_hash_value("X7Wb4")))
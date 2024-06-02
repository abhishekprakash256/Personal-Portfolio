"""
The file to make the chat app and combine all the pieces to work together 
Including the filling of the chat hash 
"""
from redis_fun.redis_helper import *
from hashing.make_hashes import * 


#const values for redis
HASH_NAME = "chat-hash"
SET_NAME = "chat-set"


helper_fun_chat_hash = Helper_fun(HASH_NAME,SET_NAME)





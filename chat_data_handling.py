"""
The chat messages data handling files for the chat-app

"""

from datetime import datetime
from mongo.mongo_helper import *


#database and collection
DATA_BASE_NAME = "test-chat-data"
COLLECTION_NAME = "test-chat-message"


#make the instance of the class
mongo_helper_class = Helper_fun()

#make the database and collection 
mongo_helper_class.make_database_and_collection(DATA_BASE_NAME,COLLECTION_NAME)




        
def retrive_message(DATA_BASE_NAME, COLLECTION_NAME, chat_hash, user_hash_1):
    """
    The retrived messages form the database
    """
    messages = mongo_helper_class.get_chat_messages(DATA_BASE_NAME, COLLECTION_NAME, chat_hash)
    formatted_messages = []
    for message in messages:
        if message['sender_hash'] == user_hash_1:
            formatted_messages.append({'type': 'sent', 'message': message["message"]})
        else:
            formatted_messages.append({'type': 'received', 'message': message["message"]})
    return formatted_messages

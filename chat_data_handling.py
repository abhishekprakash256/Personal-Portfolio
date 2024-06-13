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





def retrive_message(DATA_BASE_NAME,COLLECTION_NAME,chat_hash,user_hash_1):
    messages = mongo_helper_class.get_chat_messages(DATA_BASE_NAME,COLLECTION_NAME,chat_hash)
    for message in messages:
        if message['sender_hash'] == user_hash_1:
            print(f'Sender: {message["message"]}')
        else:
            print(f'Recipient: {message["message"]}')
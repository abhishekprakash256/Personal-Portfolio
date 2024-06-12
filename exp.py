"""
The chat storage system for the message sending and reciving
maek the dummy message, chathash, cookie hash for both users , messges

ijGTeB hi InF3ZSI.ZmkriQ.lp1JQX0LsKUsHwcJZBlc-KYlfgk

ijGTeB hello InJ0eSI.ZmksAg.t_VuaonAEQYHqy-Bbg4Sqt1NMmM

messages 
    user_1
        hi 
    
    user_2 
        hey 
        how are you ?

    user_1
        I am good 
        how u doing ? 

    user_2
        I am good any plans 


message_doc = {
    'chat_hash': chat_hash,
    'sender_hash': user_hash_1,
    'recipient_hash': user_hash_2,
    'message': message,
    'timestamp': datetime.now()
}


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



chat_hash = "9wCPZUFVNZ"

user_hash_1 = "pbkdf2:sha256:600000$3B3wNKyIrygNsAXS$714434fbb1208916051268f635e5a8865b8d9b836c2d08bfc99db3d651174580"

user_hash_2 = "pbkdf2:sha256:600000$LhLfKUG0jJfbWsF0$ab1b402e6b413916b4d69aa41b193bd22ebb4d47e5f64efaeb3b43dabb2c55c4"







#insert data in message db 
#mongo_helper_class.insert_message_data(DATA_BASE_NAME,COLLECTION_NAME,chat_hash,user_hash_1,user_hash_2,"hi")
#mongo_helper_class.insert_message_data(DATA_BASE_NAME,COLLECTION_NAME,chat_hash,user_hash_2,user_hash_1,"how are u")
#mongo_helper_class.insert_message_data(DATA_BASE_NAME,COLLECTION_NAME,chat_hash,user_hash_1,user_hash_2,"I am good")
#mongo_helper_class.insert_message_data(DATA_BASE_NAME,COLLECTION_NAME,chat_hash,user_hash_1,user_hash_2,"what about u ?")



#retrive the messages 

# Retrieve chat messages for the given chat hash
messages = mongo_helper_class.get_chat_messages(DATA_BASE_NAME,COLLECTION_NAME,chat_hash)
for message in messages:
    if message['sender_hash'] == user_hash_1:
        print(f'Sender: {message["message"]}')
    else:
        print(f'Recipient: {message["message"]}')




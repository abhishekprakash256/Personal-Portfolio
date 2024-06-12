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




"""


from datetime import datetime
chat_hash = "ijGTeB"

user_hash_1 = "InF3ZSI.ZmkriQ.lp1JQX0LsKUsHwcJZBlc-KYlfgk"

user_hash_2 = "InJ0eSI.ZmksAg.t_VuaonAEQYHqy-Bbg4Sqt1NMmM"

message = "hi"


message_doc = {
    'chat_hash': chat_hash,
    'sender_hash': user_hash_1,
    'recipient_hash': user_hash_2,
    'message': message,
    'timestamp': datetime.now()
}

print(message_doc)





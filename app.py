"""
make the main app for the website 

"""
#imports
import json
import os 
from datetime import timedelta, datetime
from itsdangerous import URLSafeTimedSerializer
from flask import Flask, render_template, request, jsonify, redirect, make_response , url_for
from read_data_mongo import get_article_data
from redis_fun.redis_helper import * 
from generate_tiny_url import * 
from chat_hash import *
from flask_socketio import SocketIO, send, emit, join_room, leave_room
from werkzeug.security import generate_password_hash, check_password_hash

#the hasing 
from hashing import *

#the database message addition test
from chat_data_handling import *



#added for eventlet 
import eventlet
#eventlet.monkey_patch()


#for test 
import json

#db names in mongo
db_name = ["articles","section"]

#collection names in database 
collections = ["projects","tech","life","section_data"]

app = Flask(__name__)

app.config['STATIC_FOLDER'] = 'static'

#for socket programming
socketio = SocketIO(app, async_mode='eventlet')




app.secret_key = 'Qwerty@8243'  # Replace with a strong, random key
serializer = URLSafeTimedSerializer(app.secret_key)



#the encryption and decryption of the cookie code 
def encrypt_cookie(value):
    return serializer.dumps(value)

def decrypt_cookie(value):
    try:
        return serializer.loads(value)  # 1 hour expiration
    except:
        return None
















#index page save_cookie
@app.route('/')
def home():
    return render_template('index.html')


#about page
@app.route('/about')
def about():
    return render_template('about.html')


#section page
@app.route('/<section_name>')
def section(section_name):

    page_data = get_article_data(db_name[1],collections[3],{'section_name': section_name})

    #print(page_data)

    return render_template('section.html',**page_data)


#article page can be projects
@app.route('/projects/<article_name>')
def projects(article_name):

    #page_data = {"articles_json": articles_json}

    data = get_article_data(db_name[0],collections[0],{'article_name': article_name}) 
    page_data2 = {"articles_json": data}

    return render_template('projects/article.html', **page_data2)



#the demo route for projects
@app.route('/demo/<project_name>')
def project_demo(project_name):
    # Define nested data dictionary with project names as keys
    demo_data = {
        'project_urls': {
            'academic-website': "projects/Academic-Website/index.html",
            'tiny-url': "demo/tiny-url/tiny_url.html",
            # Add more projects and their URLs as needed
        }
    }
    return render_template('reusable/demo.html', project_name= project_name, data=demo_data)




#article page can be tech
@app.route('/tech/<article_name>')
def tech(article_name):

    #page_data = {"articles_json": articles_json}

    data = get_article_data(db_name[0],collections[1],{'article_name': article_name}) 
    page_data2 = {"articles_json": data}

    return render_template('projects/article.html', **page_data2)




#store the data in the json file
def store_form_data(name, email, message):
    # Create a dictionary with the form data
    form_data = {
        'name': name,
        'email': email,
        'message': message
    }
    
    # Append the form data to a list or create a new list if the file doesn't exist
    form_data_list = []
    if os.path.exists('form_data.json'):
        with open('form_data.json', 'r') as list_file:
            try:
                form_data_list = json.load(list_file)
            except json.decoder.JSONDecodeError:
                pass
    
    form_data_list.append(form_data)
    
    # Write the list to the JSON file
    with open('form_data.json', 'w') as list_file:
        json.dump(form_data_list, list_file, indent=4)
    print("Form data saved to list in JSON file successfully")



#the sublit of the message route for the send message 
@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Retrieve form data
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    #the data stored in the json file 
    store_form_data(name, email, message)

    return jsonify({'success': True, 'message': 'Form data submitted successfully'})



#the submit post route for the tiny url 
@app.route('/submit_tiny_url', methods=['POST'])
def submit_tiny_url():
    # Retrieve form data
    original_url = request.form.get('original_url')

    #print(original_url)

    # Generate the tiny URL and get the hash, put in Redis 
    tiny_url = generate_tiny_url_fun(original_url)

    # Return the tiny URL hash
    return jsonify({'success': True, 'tiny_url': tiny_url})


#the function to redirect to the original url given using the https:// pasted
@app.route("/tu/<tiny_url>")
def tiny_url_redirect(tiny_url):

    # Fetch the original value from Redis
    original_url = helper_fun.get_hash_value(tiny_url)
    
    #print(original_url)
    
    return redirect(original_url)



#render the tiny url demo page
@app.route('/demo/tiny-url')
def tiny_url_render():

    return render_template('demo/tiny-url/tiny_url.html')




#-------------------- the chatting system  ---------------------

#database and collection for message data saving 
DATA_BASE_NAME = "test-chat-data"
COLLECTION_NAME = "test-chat-message"



#register the user for chat page 

@app.route('/chat_user_sign_up', methods=['POST'])
def submit_user_details():
    
    data = request.get_json()  # Retrieve JSON data from the request
    name_1 = data.get('name_1')
    name_2 = data.get('name_2')

    #make the upper and lower case
    name_1 = name_1.lower()
    name_2 = name_2.lower()


    #hash the user name 
    hashed_username_1 = generate_password_hash(name_1,method='pbkdf2:sha256')
    hashed_username_2 = generate_password_hash(name_2,method='pbkdf2:sha256')

    #generate the random hash
    chat_hash = generate_random_hash()

    #store the chat hash and the hashed uername in the redis 
    helper_fun_chat_hash.store_list_hash_val(chat_hash,[hashed_username_1,hashed_username_2])

    # Return the chat URL
    return jsonify({'success': True, 'hash': chat_hash})




#the login page for the user
#the sublit of the message route for the send message 
@app.route('/login_user', methods=['POST'])
def submit_user_login():
    
    # Retrieve form data
    user_name = request.form.get('user_name')

    #handle  the upper and lower case
    user_name = user_name.lower()

    chat_hash = request.form['chat_hash']

    #hash the username 
    hashed_username_1 = helper_fun_chat_hash.get_users_value_from_hash(chat_hash)[0]
    hashed_username_2 = helper_fun_chat_hash.get_users_value_from_hash(chat_hash)[1]

    #overridding
    #resp = make_response(jsonify({'success': True, 'message': 'Form data submitted successfully'}))
    #encrypted_value = encrypt_cookie(user_name)
    #resp.set_cookie(chat_hash,encrypted_value)


    #check for the login 
    if check_password_hash(hashed_username_1,user_name) or check_password_hash(hashed_username_2,user_name):

        #set the expiration time of the cookie 
        #expires = datetime.now() + timedelta(hours=1)  # Set the expiration time to 1 day

        resp = make_response(jsonify({'success': True, 'message': 'Form data submitted successfully', 'reload': True}))

        encrypted_value = encrypt_cookie(user_name)  

        #resp.set_cookie(chat_hash, user_name, max_age=3600, expires=expires, secure=True, httponly=True, samesite='Lax')

        resp.set_cookie(chat_hash,encrypted_value)
        return resp


    else:

        return jsonify({'success': False, 'message': 'Invalid Login'})



@app.route('/end_chat', methods=['POST'])
def end_chat():
    data = request.get_json()
    message = data.get('message')

    #delete the data from redis
    chat_hash = data['chat_hash']

    #delete the data from redis 
    helper_fun_chat_hash.delete_hash_val(data['chat_hash'])


    #delete the database of chat messages 
    mongo_helper_class.delete_message(DATA_BASE_NAME,COLLECTION_NAME,chat_hash)

    
    # Return a JSON response with the URL to redirect
    return jsonify({"status": "success", "redirect_url": url_for('chatting_start')})



#logut function 

@app.route('/log_out', methods=['POST'])
def log_out():
    data = request.get_json()
    message = data.get('message')
    chat_hash = data.get('chat_hash')

    # delete the data from Redis
    # (Add your Redis deletion logic here)

    # Return a JSON response with the URL to redirect
    # Create a response object
    resp = make_response(jsonify({"status": "success", "redirect_url": f'/chat/user/{chat_hash}'}))

    # Set the cookie with an expiration date in the past to delete it
    resp.set_cookie(chat_hash, '', expires=datetime.utcnow() - timedelta(days=1))

    return resp




@app.route('/demo/chat-app')
def chatting_start():
    
    return render_template('chatting/chat-register.html')



@socketio.on('join')
def on_join(data):
    chat_hash = data['chat_hash']
    user_id = data['user_id']

    #get the cookie value 
    cookie_val = request.cookies.get(chat_hash)
    print(cookie_val)


    join_room(chat_hash)

    #emit('status', {'msg': f'{user_id} has entered the room.'}, room = chat_hash)


@socketio.on('leave')
def on_leave(data):
    chat_hash = data['chat_hash']
    user_id = data['user_id']

    #get the cookie value 
    cookie_val = request.cookies.get(chat_hash)
    print(cookie_val)

    leave_room(chat_hash)
    
    #emit('status', {'msg': f'{user_id} has left the room.'}, room=chat_hash)




@socketio.on('message')
def handle_message(data):
    chat_hash = data['chat_hash']
    msg = data['msg']
    user_id = data['user_id']
 
    #get the cookie value 
    cookie_value = request.cookies.get(chat_hash) 
    
    #decrypt the cookie value 
    user_name = decrypt_cookie(cookie_value)

    #get the user name hashes from database 
    hashed_username_1 = helper_fun_chat_hash.get_users_value_from_hash(chat_hash)[0]
    hashed_username_2 = helper_fun_chat_hash.get_users_value_from_hash(chat_hash)[1]
    #print(hashed_username_1)
    #print(hashed_username_2)

    #the logic to flip the usename as per hash value found 
    if check_password_hash(hashed_username_1,user_name):
        user_hash_1, user_hash_2 =  hashed_username_1, hashed_username_2

    else:
        user_hash_1, user_hash_2 = hashed_username_2 , hashed_username_1


    #add the data store system here 
    mongo_helper_class.insert_message_data(DATA_BASE_NAME,COLLECTION_NAME,chat_hash,user_hash_1,user_hash_2,msg)


    #get the message data here , username is not coming rn 
    #print("all the message data",user_id,chat_hash,msg,cookie_value) #test


    emit('message', {'msg': msg, 'user_id': user_id}, room=chat_hash)




@app.route('/chat/user/<chat_hash_url>')
def chat_one(chat_hash_url):
    res = helper_fun_chat_hash.check_hash_exist(chat_hash_url)

    # Get the user cookie
    user_cookie = request.cookies.get(chat_hash_url)

    if user_cookie:
        #print("inside cookie")

        hashed_username_1 = helper_fun_chat_hash.get_users_value_from_hash(chat_hash_url)[0]
        hashed_username_2 = helper_fun_chat_hash.get_users_value_from_hash(chat_hash_url)[1]

        print(hashed_username_1)

        if not hashed_username_1 or not hashed_username_2:
            return "<h1>Chat has been ended by user</h1>"

        # Decrypt the cookie value
        user_name = decrypt_cookie(user_cookie)

        # The logic to flip the username as per hash value found
        if check_password_hash(hashed_username_1, user_name):
            user_hash_1 = hashed_username_1
        else:
            user_hash_1 = hashed_username_2

        # Retrieve messages
        messages = retrive_message(DATA_BASE_NAME, COLLECTION_NAME, chat_hash_url, user_hash_1)

        if res:
            return render_template('chatting/chat.html', chat_hash_url=chat_hash_url, messages=messages , user_name = user_name.capitalize())
        else:
            return "<h1>Chat has been ended by user</h1>"
    else:
        if res:
            return render_template('chatting/chat.html', chat_hash_url=chat_hash_url)
        else:
            return "<h1>Page not Found</h1>"






"""
@socketio.on('message')
def handle_message(msg):
    emit('message', msg, broadcast=True, include_self=False)
"""






if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
    #app.run(debug=True)
"""
make the main app for the website 

"""
#imports
import json
import os 
from flask import Flask, render_template, request, jsonify, redirect
from read_data_mongo import get_article_data
from redis_fun.redis_helper import * 
from generate_tiny_url import * 
from flask_socketio import SocketIO, send, emit

#the hasing test
from hashing import *


#added for eventlet 
import eventlet
#eventlet.monkey_patch()


#for test 
import json

#const

#db names in mongo
db_name = ["articles","section"]

#collection names in database 
collections = ["projects","tech","life","section_data"]

#redis database 




app = Flask(__name__)

app.config['STATIC_FOLDER'] = 'static'

#for socket programming
socketio = SocketIO(app, async_mode='eventlet')


#index page 
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




# -------------------- the chatting system experiments ---------------------


"""
#the one way chat sender system
@app.route('/chat/send-test')
def chatting_sender():
    return render_template('chatting/sender.html')

#the reciver end 
@app.route('/chat/receive-test')
def chatting_receive():
    return render_template('chatting/receive.html')


#mesage for the socket
@socketio.on('message')
def handle_message(msg):
    print(f'Message: {msg}')
    send(msg, broadcast=True)

    
#one person chat rteciver 
@app.route('/chat/chat-two')
def chat_two():
    return render_template('chatting/chat.html')
"""


#register the user for chat page 

@app.route('/chat_user_sign_up', methods=['POST'])
def submit_user_details():
    
    data = request.get_json()  # Retrieve JSON data from the request
    name_1 = data.get('name_1')
    name_2 = data.get('name_2')

    chat_hash = generate_random_hash()
    print(name_1)
    print(name_2)
    print(chat_hash)


    # Store the pair data in the database
   

    # Generate the chat URL


    # Return the chat URL
    return jsonify({'success': True, 'hash': chat_hash})



@app.route('/chat-start')
def chatting_start():
    return render_template('chatting/chat-register.html')



@socketio.on('message')
def handle_message(msg):
    emit('message', msg, broadcast=True, include_self=False)


#the chat end point
@app.route('/chat')
def chat_one():
    return render_template('chatting/chat.html')



if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
    #app.run(debug=True)
"""
The script to update branch , kill the server , push the database values and run the server again
"""

"""
#print('returncode:', result.returncode)
The commands to run 

git pull 
ps aux | grep flask
kil pid

cd mongo
python3 bulk_data_insertion.py

cd .. 
flask run --host=0.0.0.0 --port=5000 > output.log 2>&1 & disown

"""


import subprocess
import os


#system start the redis 
start_redis = subprocess.run(['sudo systemctl start redis-server.service'], shell=True, capture_output=True, text=True, check=True)


#system start the mongod 
start_mongo = subprocess.run(['sudo systemctl start mongod.service'], shell=True, capture_output=True, text=True, check=True)

# Running a command to pull the latest git files
git_pull = subprocess.run(['git', 'pull'], capture_output=True, text=True)

print('stdout:', git_pull.stdout)


#kill the flask server 
gunicorn_process = subprocess.run('ps aux | grep gunicorn', shell=True, capture_output=True, text=True)


gunicorn_process_pid = gunicorn_process.stdout[10:16]

print(gunicorn_process_pid)

#store the originonal directory 
original_directory = os.getcwd()


#kill the flask process
kill_gunicorn_process = subprocess.run(['kill', gunicorn_process_pid], capture_output=True, text=True)

#print(kill_flask_process.returncode)

#injets the dataset for mongo db 

injest_data = subprocess.run(['cd mongo && python3 bulk_data_insertion.py'], shell=True, capture_output=True, text=True, check=True)

print(injest_data.stdout)


#change the dir again
os.chdir(original_directory)


redis_recovery_process = subprocess.run('ps aux | grep redis_recovery_func.py', shell=True, capture_output=True, text=True)

redis_recovery_process_pid = redis_recovery_process.stdout[11:16]

print(redis_recovery_process_pid)

#kill the recovery process process
kill_redis_recovery_process = subprocess.run(['kill', redis_recovery_process_pid], capture_output=True, text=True)


#run the redis recovery system 
redis_recovery = subprocess.run(['cd redis_recovery && nohup python3 redis_recovery_func.py > output.log 2>&1 &'], shell=True, capture_output=True, text=True, check=True)


#change the dir again
os.chdir(original_directory)


#run the flask server again

run_server = subprocess.run('nohup gunicorn --worker-class eventlet -w 1 -b 0.0.0.0:5000 wsgi:app > gunicorn.log 2>&1 &', shell=True, check=True)
if run_server:
    print("Server started succesfully")

else:
    print("Failed to start  server")

#!/bin/bash

# Start MongoDB
mongod --fork --logpath /var/log/mongodb.log --dbpath /var/lib/mongodb

# Start Redis
redis-server --daemonize yes

# Start Flask application
exec python app.py

#!/bin/sh

# Wait for MongoDB to be ready
while ! nc -z mongo 27017; do
  echo "Waiting for MongoDB..."
  sleep 2
done

# Wait for Redis to be ready
while ! nc -z redis 6379; do
  echo "Waiting for Redis..."
  sleep 2
done

# Start the Flask app
exec flask run

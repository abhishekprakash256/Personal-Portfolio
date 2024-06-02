import redis
import json

r = redis.Redis(host='localhost', port=6379, db=0,decode_responses=True)

# Data to store
data = ["Abhi", "anny"]

# Convert the list to a JSON string
data_str = json.dumps(data)

# Set the JSON string in the Redis hash
r.hset('test-hash', 'name2', data_str)

# Retrieve the JSON string from the Redis hash
retrieved_data_str = r.hget('test-hash', 'name2')

# Convert the JSON string back to a list
retrieved_data = json.loads(retrieved_data_str)

print(retrieved_data)  # Output: ["Abhi", "anny"]

# Check if a field exists in the hash
field_exists = r.hexists('test-hash', 'name2')

if field_exists:
    print("The field 'name2' exists in the hash 'test-hash'.")
else:
    print("The field 'name2' does not exist in the hash 'test-hash'.")
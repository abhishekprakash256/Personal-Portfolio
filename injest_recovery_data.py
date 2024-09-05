"""
injest the recovery data
"""

import subprocess


#mongo data injest
mongo_injest_data = subprocess.run(['docker cp ./redis-backups/dump.rdb redis:/data/dump.rdb'], shell=True, capture_output=True, text=True, check=True)
print(mongo_injest_data)

#redis data copy
redis_data_copy = subprocess.run(['docker cp redis:/data/dump.rdb ./redis-backups/dump.rdb'], shell=True, capture_output=True, text=True, check=True)
print(redis_data_copy)

#redis injest data
redis_injest_data = subprocess.run(['docker cp ./redis-backups/dump.rdb redis:/data/dump.rdb'], shell=True, capture_output=True, text=True, check=True)
print(redis_injest_data)
"""
Make a recovery service for the redis and mogno container 
"""
"""
the steps - 
- #mongo
-- creating backups (auotmated)
    - docker exec mongo mongodump --out /backup/db-backup

#redis
- creating backups (automate)
    - docker exec redis redis-cli BGSAVE

- copy the file from container to host (automate)
    - docker cp redis:/data/dump.rdb ./redis-backups/dump.rdb


"""



import subprocess
import os
import time


#time duration of 10 seonds
TIME_DURATION = 30


def backup_databases():

    # Create MongoDB backup
    mongo_backup = subprocess.run(['docker exec mongo mongodump --out /backup/db-backup'], shell=True, capture_output=True, text=True, check=True)
    print("MongoDB Backup: ", mongo_backup)
    
    # Create Redis backup
    redis_backup = subprocess.run(['docker exec redis redis-cli BGSAVE'], shell=True, capture_output=True, text=True, check=True)
    print("Redis Backup: ", redis_backup)
    
    # Copy Redis backup file to host
    redis_copy = subprocess.run(['docker cp redis:/data/dump.rdb ./redis-backups/dump.rdb'], shell=True, capture_output=True, text=True, check=True)
    print("Redis Backup Copy: ", redis_copy)




def run_periodically(duration):
    """
    The function to run the recovery system periodically 
    """
    while True:
        # Run your code here
        try:
        
            #save the redish hash to json 
            backup_databases()
            print("Running the script...")

        except Exception as e:
            print(f"An error occurred: {e}")

        # Wait for 10 seconds
        time.sleep(duration)  # 10 seconds


if __name__ == "__main__":
    run_periodically(TIME_DURATION)








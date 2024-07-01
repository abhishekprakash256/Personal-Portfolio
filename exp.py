
import subprocess
import os


redis_recovery_process = subprocess.run('ps aux | grep redis_recovery_func.py', shell=True, capture_output=True, text=True)

#get the pid
print(redis_recovery_process.stdout)

redis_recovery_process_pid = redis_recovery_process.stdout[11:16]

print(redis_recovery_process_pid)

#kill the recovery process process
kill_redis_recovery_process = subprocess.run(['kill', redis_recovery_process_pid], capture_output=True, text=True)

print(kill_redis_recovery_process)
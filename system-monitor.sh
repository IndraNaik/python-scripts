#!/usr/bin/env python3

import shutil

THRESHOLD = 80
print("Checking disk usage...")

partitions = shutil.disk_usage('/')
total, used, free = partitions.total, partitions.used, partitions.free
usage_percent = int((used / total) * 100)

if usage_percent >= THRESHOLD:
    print(f"Warning: Disk usage is at {usage_percent}%")
else:
    print(f"Disk usage is within limits: {usage_percent}%")

===============================================================================

#!/usr/bin/env python3

import os

THRESHOLD = 100  # in MB
print("Checking memory usage...")

with os.popen("free -m | awk '/^Mem:/ {print $4}'") as stream:
    free_mem = int(stream.read().strip())

if free_mem <= THRESHOLD:
    print(f"Warning: Free memory is below {THRESHOLD}MB. Current free memory: {free_mem}MB")
else:
    print(f"Memory usage is within safe limits. Current free memory: {free_mem}MB")

===============================================================================================

#!/usr/bin/env python3

import subprocess

PROCESS_NAME = "nginx"

def is_running(process):
    result = subprocess.run(["pgrep", process], stdout=subprocess.DEVNULL)
    return result.returncode == 0

if is_running(PROCESS_NAME):
    print(f"{PROCESS_NAME} is running.")
else:
    print(f"{PROCESS_NAME} is not running. Attempting to start...")
    subprocess.run(["sudo", "systemctl", "start", PROCESS_NAME])
    print(f"{PROCESS_NAME} started.")
